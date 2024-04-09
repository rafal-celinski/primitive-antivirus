import pytest
from src.cyclic_scan_config import CyclicScanConfig
import src.file_interface as file_interface
from pathlib import Path

CYCLIC_SCAN_CONFIG_PATH = 'tests/files/index/cyclic_scan_config.json'


@pytest.fixture(scope="session")
def cyclic_scan_config_path(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp('resources') / 'cyclic_scan_config.json'
    cyclic_scan_config_content = file_interface.readJson(
        CYCLIC_SCAN_CONFIG_PATH)
    file_interface.saveToJson(cyclic_scan_config_content, tmp_path)
    return tmp_path


@pytest.fixture()
def cyclic_scan_config(cyclic_scan_config_path):
    cyclic_scan_config = CyclicScanConfig(cyclic_scan_config_path)
    return cyclic_scan_config


def test_init_without_path():
    cyclic_scan_config = CyclicScanConfig()
    assert cyclic_scan_config._index == {
            "frequency": -1,
            "fast_scan": False,
            "last_scan": 0,
            "paths_to_scan": []
        }


def test_frequency(cyclic_scan_config):
    assert cyclic_scan_config.frequency() == 31


def test_fastScan(cyclic_scan_config):
    assert cyclic_scan_config.fastScan() is True


def test_lastScan(cyclic_scan_config):
    assert cyclic_scan_config.lastScan() == 123456


def test_pathsToScan(cyclic_scan_config):
    assert cyclic_scan_config.pathsToScan() == \
        [Path("path1"), Path("Path2"), Path("Path3")]


def test_setFrequency(cyclic_scan_config):
    cyclic_scan_config.setFrequency(20)
    assert cyclic_scan_config.frequency() == 20


def test_setFastScan(cyclic_scan_config):
    cyclic_scan_config.setFastScan(False)
    assert cyclic_scan_config.fastScan() is False


def test_setLastScan(cyclic_scan_config):
    cyclic_scan_config.setLastScan(999999)
    assert cyclic_scan_config.lastScan() == 999999


def test_setPathToScan(cyclic_scan_config):
    cyclic_scan_config.setPathsToScan([Path("path4"), Path("path5")])
    assert cyclic_scan_config.pathsToScan() == [Path("path4"), Path("Path5")]


def test_validateFile(cyclic_scan_config):
    assert cyclic_scan_config.validateFile() is True


def test_validateFile_incorrect(cyclic_scan_config, monkeypatch):
    monkeypatch.setattr(cyclic_scan_config, '_index', {"key": 'value'})
    assert cyclic_scan_config.validateFile() is False
