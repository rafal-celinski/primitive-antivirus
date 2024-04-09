from pathlib import Path
from src.scan import Scan
from src.file_index import FileIndex
from src.threat_index import ThreatIndex
from src.log import LogInterface
import src.file_interface as file_interface


# LogInterface class is abstract and for testing we need concrete class
class LogForTests(LogInterface):
    def fileError(self, file_path): pass
    def dirError(self, dir_path): pass
    def fileScanning(self, file_path): pass
    def threatFound(self, file_path, threat_id): pass
    def scanningComplete(self): pass
    def scanningAborted(self): pass


# Constance paths to test files
FILE_INDEX_PATH = Path('tests/files/scan/files.json')
THREAT_INDEX_PATH = Path('tests/files/scan/threats.json')
DIR_TO_SCAN_PATH = Path('tests/files/scan/dir_to_scan')
EICAR_FILE_PATH = DIR_TO_SCAN_PATH / Path('eicar_test_file.txt')
SAFE_FILE_PATH = DIR_TO_SCAN_PATH / Path('safe.txt')
SAFE2_FILE_PATH = DIR_TO_SCAN_PATH / Path('safe2.txt')
FIXED_EICAR_PATH = Path('tests/files/scan/fixed_eicar.txt')


def test_toScanning_normal_scan(monkeypatch):
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    monkeypatch.setattr(scanner, '_fast_scan', False)
    assert scanner._toScanning(EICAR_FILE_PATH) is True
    assert scanner._toScanning(SAFE_FILE_PATH) is True
    assert scanner._toScanning(SAFE2_FILE_PATH) is True


def test_toScanning_fast_scan(monkeypatch):
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    monkeypatch.setattr(scanner, '_fast_scan', True)
    assert scanner._toScanning(EICAR_FILE_PATH) is False
    assert scanner._toScanning(SAFE_FILE_PATH) is True
    assert scanner._toScanning(SAFE2_FILE_PATH) is True


def test_scan_dir_normal():
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    assert scanner.scan([DIR_TO_SCAN_PATH], False) == [(EICAR_FILE_PATH, 0)]


def test_scan_dir_fast():
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    assert scanner.scan([DIR_TO_SCAN_PATH], True) == []


def test_scan_file_normal():
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    assert scanner.scan([EICAR_FILE_PATH], False) == [(EICAR_FILE_PATH, 0)]
    assert scanner.scan([SAFE_FILE_PATH], False) == []
    assert scanner.scan([SAFE2_FILE_PATH], False) == []


def test_scan_file_list():
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    assert scanner.scan([EICAR_FILE_PATH, SAFE_FILE_PATH, SAFE2_FILE_PATH], False) == [(EICAR_FILE_PATH, 0)]  # noqa: E501


def test_scan_file_fast():
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)
    assert scanner._toScanning(EICAR_FILE_PATH)
    assert scanner.scan([EICAR_FILE_PATH], True) == []
    assert scanner.scan([SAFE_FILE_PATH], True) == []
    assert scanner.scan([SAFE2_FILE_PATH], True) == []


def test_fixFile(tmp_path_factory):
    file_to_fix = tmp_path_factory.mktemp('resources') / 'eicar.txt'
    file_content = file_interface.openFileAsHex(EICAR_FILE_PATH)
    file_interface.writeHexToFile(file_to_fix, file_content)
    file_index = FileIndex(FILE_INDEX_PATH)
    threat_index = ThreatIndex(THREAT_INDEX_PATH)
    log = LogForTests()
    scanner = Scan(file_index, threat_index, log)

    scanner.fixFile(file_to_fix, 0)

    assert file_interface.openFileAsHex(file_to_fix) == \
        file_interface.openFileAsHex(FIXED_EICAR_PATH)
