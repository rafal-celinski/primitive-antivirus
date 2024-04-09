import pytest
import json
from src.json_index import JsonIndex

JsonIndex.__abstractmethods__ = set()

CORRECT_JSON_PATH = 'tests/files/index/correct.json'
INCORRECT_JSON_PATH = 'tests/files/index/incorrect.json'
EMPTY_JSON_PATH = 'tests/files/index/empty.json'


def test_correct_json():
    json_index = JsonIndex(CORRECT_JSON_PATH)
    assert json_index._index == {
                                    "key1": "value1",
                                    "key2": "value2",
                                    "key3": "value3"
                                }


def test_incorrect_json():
    with pytest.raises(json.decoder.JSONDecodeError):
        JsonIndex(INCORRECT_JSON_PATH)


def test_empty_json():
    with pytest.raises(json.decoder.JSONDecodeError):
        JsonIndex(EMPTY_JSON_PATH)


def test_backupIndex():
    file_index = JsonIndex(CORRECT_JSON_PATH)
    assert file_index._index == {
                                    "key1": "value1",
                                    "key2": "value2",
                                    "key3": "value3"
                                }
    file_index.backupIndex()
    assert file_index._backup == {
                                    "key1": "value1",
                                    "key2": "value2",
                                    "key3": "value3"
                                 }


def test_restoreBackup():
    file_index = JsonIndex(CORRECT_JSON_PATH)
    file_index.backupIndex()
    file_index._index = {}
    assert file_index._index == {}
    assert file_index._backup == {
                                    "key1": "value1",
                                    "key2": "value2",
                                    "key3": "value3"
                                 }
    file_index.restoreBackup()
    assert file_index._index == {
                                    "key1": "value1",
                                    "key2": "value2",
                                    "key3": "value3"
                                 }
