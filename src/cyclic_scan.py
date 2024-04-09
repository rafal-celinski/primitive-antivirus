from src.cyclic_scan_config import CyclicScanConfig
from typing import List
from pathlib import Path
import time


class CyclicScan():
    def __init__(self, config_object: CyclicScanConfig):
        self._config = config_object

    def setConfig(self, frequency: int, fast_scan: bool,
                  paths_to_scan: List[Path]):
        self._config.setFrequency(frequency)
        self._config.setFastScan(fast_scan)
        self._config.setPathsToScan(paths_to_scan)

    def isScanNeeded(self) -> bool:
        if self._config.frequency() == -1:
            return False
        else:
            return self._config.lastScan() + \
                self._config.frequency() * 24*60*60 < int(time.time())

    def fastScan(self) -> bool:
        return self._config.fastScan()

    def pathsToScan(self) -> List[Path]:
        return self._config.pathsToScan()

    def scannedNow(self):
        self._config.setLastScan(int(time.time()))
