from pathlib import Path
from typing import Tuple, List
from PySide6.QtCore import QObject, Signal
from src.scan import Scan
from src.file_index import FileIndex
from src.threat_index import ThreatIndex
from src.log import LogInterface


# A class inheriting from Loginterface, emitting ScanQt class signals
class LogQt(LogInterface):
    def __init__(self, scan_qt): self.ScanQt = scan_qt
    def fileError(self, file: Path): self.ScanQt.fileError.emit(file)
    def dirError(self, dir: Path): self.ScanQt.dirError.emit(dir)
    def fileScanning(self, file: Path): self.ScanQt.fileScanning.emit(file)
    def threatFound(self, file: Path, threat_id: int): self.ScanQt.threatFound.emit(file, threat_id)  # noqa: E501
    def scanningComplete(self): self.ScanQt.scanningComplete.emit()
    def scanningAborted(self): self.ScanQt.scanningAborted.emit()


class ScanQt(QObject):
    fileError = Signal(Path)
    dirError = Signal(Path)
    fileScanning = Signal(Path)
    threatFound = Signal(Path, int)
    scanningComplete = Signal()
    scanningAborted = Signal()

    def __init__(self, file_index: FileIndex, threat_index: ThreatIndex):
        super().__init__()
        self.log = LogQt(self)
        self.scanner = Scan(file_index, threat_index, self.log)

    def scan(self, paths: List[Path], fast_scan: bool = False) -> List[Tuple[Path, int]]:  # noqa: E501
        return self.scanner.scan(paths, fast_scan)

    def stop(self):
        self.scanner.stop()

    def fixFile(self, file: Path, threat_id: int):
        self.scanner.fixFile(file, threat_id)
