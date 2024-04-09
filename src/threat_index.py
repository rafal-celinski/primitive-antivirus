from src.json_index import JsonIndex
from typing import List, Tuple


class ThreatIndex(JsonIndex):
    def addThreat(self, value: str, description: str):
        """Adds threat to index"""
        if self._index.keys():
            id = str(max([int(key) for key in self._index.keys()]) + 1)
        else:
            id = '0'
        self._index[id] = {}
        self._index[id]["value"] = value
        self._index[id]["description"] = description

    def value(self, id: int) -> str:
        id = str(id)
        return self._index[id]["value"]

    def description(self, id: int) -> str:
        id = str(id)
        return self._index[id]["description"]

    def threatList(self) -> List[Tuple[int, str]]:
        """Returns list of tuples with threat id and value"""
        return [(int(id), self.value(id)) for id in self._index.keys()]

    def _createEmptyIndex(self):
        self._index = {}
