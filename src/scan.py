import src.file_interface as file_interface
from src.file_index import FileIndex
from src.threat_index import ThreatIndex
from src.log import LogInterface
from pathlib import Path
from typing import Tuple, List
import time


class Scan:
    def __init__(self, file_index: FileIndex, threat_index: ThreatIndex, log: LogInterface):  # noqa: E501
        self._file_index = file_index
        self._threat_index = threat_index
        self._suspect_files = []
        self._fast_scan = False
        self._log = log
        self._stop_flag = False

    def scan(self, paths: List[Path], fast_scan: bool = False) -> List[Tuple[Path, int]]:  # noqa: E501
        """Checks if path is a dir or a file, and calls appropriate function.
            Returns list with threats found"""
        self._stop_flag = False
        self._file_index.backupIndex()
        self._suspect_files = []
        self._fast_scan = fast_scan
        for path in paths:
            if self._stop_flag is True:
                break
            if path.is_file():
                if self._toScanning(path):
                    self._scanFile(path)
            else:
                self._scanDir(path)

        if self._stop_flag is True:
            self._file_index.restoreBackup()  # If the scan was aborted, _file_index is restored to state before scan # noqa: E501
            self._log.scanningAborted()
            return []

        self._log.scanningComplete()
        return self._suspect_files

    def stop(self):
        self._stop_flag = True

    def fixFile(self, file: Path, threat_id: int):
        """Removes hreatening fragment in file"""
        file_content = file_interface.openFileAsHex(file)
        file_content = file_content.replace(self._threat_index.value(threat_id), '')  # Replace the threatening fragment with an empty string # noqa: E501
        file_interface.writeHexToFile(file, file_content)

    def _toScanning(self, file: Path) -> bool:
        """Checks if file needs to be scaned"""
        if file not in self._file_index:  # file doesn't exist in index, so never scanned # noqa: E501
            return True

        file_modification = int(file_interface.lastModification(file))
        file_scan = self._file_index.lastScan(file)

        if file_modification > file_scan:  # file modified since last scan
            return True

        return not self._fast_scan

    def _scanDir(self, dir: Path):
        """Scans files in directory"""
        if self._stop_flag is True:
            return
        try:
            files, directories = file_interface.filesInDir(dir)
        except PermissionError:
            self._log.dirError(dir)
            return
        for file in files:  # file scanning
            if self._toScanning(file):
                self._scanFile(file)

        for dir_to_scan in directories:  # dir scanning
            self._scanDir(dir_to_scan)

    def _scanFile(self, file: Path):
        """Scans single file"""
        if self._stop_flag is True:
            return
        self._log.fileScanning(file)
        try:
            file_content = file_interface.openFileAsHex(file)
        except PermissionError:
            self._log.fileError(file)
        else:
            for id, value in self._threat_index.threatList():
                if value in file_content:
                    self._suspect_files.append((file, id))
                    self._log.threatFound(file, id)
                    break
            self._file_index.updateFileIndex(file, int(time.time()))
