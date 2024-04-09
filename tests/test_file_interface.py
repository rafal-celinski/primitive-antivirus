from src.file_interface import filesInDir
from pathlib import Path

DIR_TO_SCAN_PATH = Path('tests/files/scan/dir_to_scan')
EICAR_FILE_PATH = DIR_TO_SCAN_PATH / Path('eicar_test_file.txt')
SAFE_FILE_PATH = DIR_TO_SCAN_PATH / Path('safe.txt')
SAFE2_FILE_PATH = DIR_TO_SCAN_PATH / Path('safe2.txt')
DIR_PATH = DIR_TO_SCAN_PATH / Path('dir')


def test_filesInDir():
    files, dirs = filesInDir(DIR_TO_SCAN_PATH)
    assert files == [EICAR_FILE_PATH, SAFE_FILE_PATH, SAFE2_FILE_PATH]
    assert dirs == [DIR_PATH]


def test_filesInDir2():
    files, dirs = filesInDir(DIR_PATH)
    assert files == [DIR_PATH / Path('safe.txt')]
    assert dirs == []
