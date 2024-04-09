from src.json_index import JsonIndex
from pathlib import Path


class FileIndex(JsonIndex):
    def updateFileIndex(self, file: Path, last_scan: int):
        """Updates information about the file in index"""
        self._index[str(file)] = {}
        self._index[str(file)]['last_scan'] = last_scan

    def lastScan(self, file: Path) -> int:
        return self._index[str(file)].get('last_scan', 0)

    def __contains__(self, file: Path) -> bool:
        return str(file) in self._index

    def _createEmptyIndex(self):
        self._index = {}
