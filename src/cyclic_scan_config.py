from src.json_index import JsonIndex
from pathlib import Path
from typing import List


class CyclicScanConfig(JsonIndex):
    def setFrequency(self, frequency: int):
        self._index["frequency"] = frequency

    def setFastScan(self, fast_scan: bool):
        self._index["fast_scan"] = fast_scan

    def setLastScan(self, last_scan: int):
        self._index["last_scan"] = last_scan

    def setPathsToScan(self, paths_to_scan: List[Path]):
        self._index["paths_to_scan"] = [str(path) for path in paths_to_scan]

    def frequency(self) -> int:
        return self._index["frequency"]

    def fastScan(self) -> bool:
        return self._index['fast_scan']

    def lastScan(self) -> int:
        return self._index['last_scan']

    def pathsToScan(self) -> List[Path]:
        paths = self._index["paths_to_scan"]
        return [Path(path) for path in paths]

    def _createEmptyIndex(self):
        self._index = {
            "frequency": -1,
            "fast_scan": False,
            "last_scan": 0,
            "paths_to_scan": []
        }

    def validateFile(self) -> bool:
        """Checks if _index includes all needed keys"""
        return "frequency" in self._index \
               and "fast_scan" in self._index \
               and "last_scan" in self._index \
               and "paths_to_scan" in self._index
