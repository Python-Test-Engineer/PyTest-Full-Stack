"""Test config"""

from utils.read_config import get_version

from rich.console import Console

console = Console()
# a config file can be a useful way to add all the CLI options we might want to pass in and can be edited manuall or have a GUI to do this.abs

# Later on, we can see how we could specify a config file in the command line that would have all options and their default values


# An example to show using configparser with config.ini file
# get_version() is in utils/read_config.py
def test_0011_SET_get_version():
    version = get_version()
    console.print(f"[blue]Version: {version}[/]")
    assert version
