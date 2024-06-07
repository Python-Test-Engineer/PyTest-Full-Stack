import warnings
import pytest


def api_v1():
    # Generates a warning with a specific message.
    warnings.warn("api v1, should use functions from v2", UserWarning)
    return 1


@pytest.mark.filterwarnings("ignore:api v1")
def test_one():
    # Will ignore warnings with the message containing "api v1".
    assert api_v1() == 1
