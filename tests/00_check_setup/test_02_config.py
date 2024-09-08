"""Test config"""
from utils.read_config import get_version

from rich.console import Console

console = Console()

# An example to show using configparser with config.ini file
def test_0011_SET_get_version():
    version = get_version()
    console.print(f"[blue]Version: {version}[/]")
    assert version
