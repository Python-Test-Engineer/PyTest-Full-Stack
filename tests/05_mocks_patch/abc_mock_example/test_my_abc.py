"""Test Interface"""
from unittest.mock import MagicMock

from my_abc import AbstractAdder, add_executer


def test_0113_add_executer_call_ad_and_returns_result() -> None:
    """Test"""
    mock_adder = MagicMock(AbstractAdder)
    mock_adder.add = MagicMock(return_value=3)
    result = add_executer(mock_adder)
    mock_adder.add.assert_called_once_with(1, 2)
    assert result == 3
