import pytest
from app.io.input import *

def test_read_from_non_existing_file():
    with pytest.raises(FileNotFoundError):
        read_from_file("BadPath.txt")

def test_read_from_bad_format_file_using_pandas():
    with pytest.raises(ValueError):
        read_with_pandas("SomeFile.json")

def test_read_from_existing_file_but_bad_path():
    with pytest.raises(FileNotFoundError):
        read_from_file("Interesting_info_to_read.txt")