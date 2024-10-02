"""Test reading of config.ini file"""

from utils.read_config import get_version, get_pet_api_url

from rich.console import Console

console = Console()
# a config file can be a useful way to add all the CLI options we might want to pass in and can be edited manuall or have a GUI to do this.abs

# Later on, we can see how we could specify a config file in the command line that would have all options and their default values


# An example to show using configparser with config.ini file
# get_version() is in utils/read_config.py
def test_0011_SET_get_version():
    version = get_version()
    console.print(f"\n[yellow]Version: {version}[/]")
    assert version == "1.0.0"


def test_0012_SET_get_pet_api_url():
    api_url = get_pet_api_url()
    console.print(f"\n[yellow]API_URL: {api_url}[/]")
    assert api_url == "https://petstore.swagger.io/v2/pet/"
