"""Test joke"""
import unittest
from unittest.mock import MagicMock, patch

import pytest

from src.joke_mock_01.api_joke import get_joke
from src.joke_mock_01.joke import len_joke


class TestJoke(unittest.TestCase):
    """Test joke"""

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_01.joke.get_joke")
    def test_0120_len_joke(self, mock_get_joke) -> None:
        """get len test"""
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_01.api_joke.requests")
    def test_0121_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        # self.assertEqual(get_joke(), {"joke": "Hello World"})
        assert get_joke() == {"joke": "Hello World"}
        assert mock_response.status_code == 200

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_01.api_joke.requests")
    def test_0122_fail_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "NO_JOKE")
        # self.assertEqual(mock_response.status_code , 200)
