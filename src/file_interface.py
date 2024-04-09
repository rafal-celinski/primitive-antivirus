import os
import json
from pathlib import Path
from typing import Tuple, List


def filesInDir(dir: Path) -> Tuple[List[Path], List[Path]]:
    """Returns tuple with lists of files in directory
    and directories in directory"""
    files = [f for f in dir.iterdir() if f.is_file()]   # only files list # noqa: E501
    dirs = [d for d in dir.iterdir() if d.is_dir()]  # only dirs list # noqa: E501
    return files, dirs


def lastModification(file: Path) -> int:
    """Returns date when the file was modified (in Unix time)"""
    return int(os.path.getmtime(file))


def saveToJson(struct, file: Path):
    """Saves structure to file"""
    with open(file, "w") as f:
        json.dump(struct, f)


def readJson(file: Path):
    """Returns structure with the contents of json file"""
    with open(file, 'r') as f:
        json_text = f.read()
    struct = json.loads(json_text)
    return struct


def openFileAsHex(file: Path) -> str:
    """Opens file as binary, read content,
    convert it to hex and saves to string"""
    with open(file, 'rb') as f:  # open file to read in binary mode
        file_content = f.read().hex()  # read file and save as hex to string
    return file_content


def writeHexToFile(file: Path, hex_notation: str):
    """Writes binary to file.
    Binary is a hexadecimal notation written as a string"""
    with open(file, 'wb') as f:
        f.write(bytes.fromhex(hex_notation))
