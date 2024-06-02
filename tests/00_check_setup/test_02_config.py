"""Some assert examples"""

from utils.read_config import get_version


def test_900_get_version():
    version = get_version()
    assert version
