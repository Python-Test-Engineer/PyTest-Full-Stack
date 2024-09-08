"""docstring"""

import sys

import pytest
from .sample import add


@pytest.mark.skip(reason="just wanna skip it")
def test_1098_add_num() -> None:
    """docstring"""
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 7), reason="use python 3.7 or less")
def test_1099_add_str() -> None:
    """docstring"""
    assert add("a", "b") == "ab"
