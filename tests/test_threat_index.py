import pytest
from src.threat_index import ThreatIndex
import src.file_interface as file_interface

THREAT_INDEX_PATH = 'tests/files/index/threat_index.json'


@pytest.fixture(scope="session")
def threat_index_path(tmp_path_factory):
    tmp_path = tmp_path_factory.mktemp('resources') / 'threat_index.json'
    threat_index_content = file_interface.readJson(THREAT_INDEX_PATH)
    file_interface.saveToJson(threat_index_content, tmp_path)
    return tmp_path


@pytest.fixture()
def threat_index(threat_index_path):
    threat_index = ThreatIndex(threat_index_path)
    return threat_index


def test_init_without_path():
    threat_index = ThreatIndex()
    assert threat_index.isEmpty() is True


def test_value(threat_index):
    assert threat_index.value(0) == 'threat_0_value'
    assert threat_index.value(2) == 'threat_2_value'


def test_value_wrong_key(threat_index):
    with pytest.raises(KeyError):
        threat_index.value(1)


def test_description(threat_index):
    assert threat_index.description(0) == 'threat_0_description'
    assert threat_index.description(2) == 'threat_2_description'


def test_description_wrong_key(threat_index):
    with pytest.raises(KeyError):
        threat_index.description(1)


def test_ThreatList(threat_index):
    assert threat_index.threatList() == [
        (0, 'threat_0_value'),
        (2, 'threat_2_value')]


def test_addThreat(threat_index):
    threat_index.addThreat('new_value', 'new_description')
    assert threat_index.threatList() == [
        (0, 'threat_0_value'),
        (2, 'threat_2_value'),
        (3, 'new_value')]
    assert threat_index.value(3) == 'new_value'
    assert threat_index.description(3) == 'new_description'
