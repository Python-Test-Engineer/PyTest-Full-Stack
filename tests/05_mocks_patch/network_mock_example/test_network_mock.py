"""Network Test"""

from unittest.mock import MagicMock

from network_mock import get_url


def test_0130_api_calls_gets_result(monkeypatch):
    """Test"""
    mock_result = MagicMock()
    mock_result.text = "Hello World"
    mock_result.timout = 10
    mock_get = MagicMock(return_value=mock_result)
    monkeypatch.setattr("requests.get", mock_get)
    result = get_url("http://www.cnn.com", timeout=10)
    mock_get.assert_called_once_with("http://www.cnn.com", timeout=10)
    assert result.text == "Hello World"
