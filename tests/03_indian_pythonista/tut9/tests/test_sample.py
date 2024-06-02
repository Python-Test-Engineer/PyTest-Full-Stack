"""Test"""

from unittest import mock

import pytest
from tut9.myapp.sample import get_ip, guess_number


@pytest.mark.parametrize("_input,expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("tut9.myapp.sample.roll_dice")
def test_0112_guess_number(mock_roll_dice, _input, expected):
    """docstring"""
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()


@mock.patch("tut9.myapp.sample.requests.get")
def test_0113_get_ip(mock_requests_get):
    """docstring"""

    mock_requests_get.return_value = mock.Mock(
        name="mock response",
        **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}}
    )

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip", timeout=5)
