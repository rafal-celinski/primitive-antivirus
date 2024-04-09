from abc import ABC, abstractmethod
from pathlib import Path


class LogInterface(ABC):
    @abstractmethod
    def fileError(self, file: Path):
        pass

    @abstractmethod
    def dirError(self, dir: Path):
        pass

    @abstractmethod
    def fileScanning(self, file: Path):
        pass

    @abstractmethod
    def threatFound(self, file: Path, threat_id: int):
        pass

    @abstractmethod
    def scanningComplete(self):
        pass

    @abstractmethod
    def scanningAborted(self):
        pass
