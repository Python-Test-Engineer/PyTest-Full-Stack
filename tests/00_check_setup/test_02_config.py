"""Some assert examples"""

import pytest

from rich.console import Console

console = Console()
from utils.read_config import get_version


def test_0011_SET_get_version():
    """An example to show using configparser with config.ini file"""
    version = get_version()
    console.print(f"[blue]Version: {version}[/]")
    assert version
