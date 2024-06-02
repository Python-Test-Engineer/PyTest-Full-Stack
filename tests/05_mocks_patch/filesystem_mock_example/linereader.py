"""Test"""

import os


def read_from_file(filename: str) -> str:
    """Test"""
    if not os.path.exists(filename):
        raise FileNotFoundError("Bad path!")
    infile = open(filename, "r", encoding="utf-8")
    line = infile.readline()
    infile.close()
    return line


def read_from_file_using_with(filename: str) -> str:
    """Test"""
    if not os.path.exists(filename):
        raise FileNotFoundError("Bad path!")
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()
        return line
