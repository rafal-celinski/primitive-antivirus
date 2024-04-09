import src.file_interface as file_interface
from src.exceptions import FileContentError
from pathlib import Path
from copy import copy
from abc import ABC, abstractmethod


class JsonIndex(ABC):
    def __init__(self, index_file: Path = None):
        """Reads index from file and saves to dict,
        if index_file_path is None, creates empty dict"""
        if index_file:
            self._index = file_interface.readJson(index_file)
        else:
            self._createEmptyIndex()

        if type(self._index) is not dict:
            raise FileContentError("The file must contain a dictionary")

    def save(self, index_file: Path):
        """Saves dict to file"""
        file_interface.saveToJson(self._index, index_file)

    def isEmpty(self) -> bool:
        return self._index == {}

    def backupIndex(self):
        self._backup = copy(self._index)

    def restoreBackup(self):
        try:
            self._index = copy(self._backup)
        except AttributeError:
            pass

    @abstractmethod
    def _createEmptyIndex(self):
        pass
