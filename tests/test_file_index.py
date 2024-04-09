import pytest
from src.file_index import FileIndex
import src.file_interface as file_interface
from pathlib import Path

FILE_INDEX_PATH = 'tests/files/index/file_index.json'


@pytest.fixture(scope="session")
def file_index_path(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp('resources') / 'file_index.json'
    file_index_content = file_interface.readJson(FILE_INDEX_PATH)
    file_interface.saveToJson(file_index_content, tmp_path)
    return tmp_path


@pytest.fixture()
def file_index(file_index_path):
    file_index = FileIndex(file_index_path)
    return file_index


def test_init_without_path():
    file_index = FileIndex()
    assert file_index.isEmpty() is True


def test_contains(file_index):
    assert Path('file_path1') in file_index
    assert Path('file_path2') in file_index
    assert Path('other_path') not in file_index


def test_lastScan(file_index):
    assert file_index.lastScan(Path('file_path1')) == 1
    assert file_index.lastScan(Path('file_path2')) == 2


def test_lastScan_nonexistent_path(file_index):
    assert Path('nonexistent_path') not in file_index
    with pytest.raises(KeyError):
        file_index.lastScan(Path('nonexistent_path'))


def test_updateFileIndex_existent_path(file_index):
    assert Path('file_path3') in file_index
    assert file_index.lastScan(Path('file_path3')) == 3
    file_index.updateFileIndex(Path('file_path3'), 10)
    assert file_index.lastScan(Path('file_path3')) == 10


def test_updateFileIndex_new_path(file_index):
    assert Path('new_path') not in file_index
    file_index.updateFileIndex(Path('new_path'), 20)
    assert Path('new_path') in file_index
    assert file_index.lastScan(Path('new_path')) == 20
