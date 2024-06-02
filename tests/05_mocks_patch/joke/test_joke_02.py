"""Test joke2 for Exceptions"""
import unittest
from unittest.mock import MagicMock, patch

import pytest
import requests.exceptions
from requests.exceptions import Timeout

from src.joke_mock_02.api_joke2 import get_joke2
from src.joke_mock_02.joke2 import len_joke2


class TestJoke(unittest.TestCase):
    """Test joke"""

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_02.joke2.get_joke2")
    def test_0123_len_joke2(self, mock_get_joke) -> None:
        """get len test"""
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke2(), 3)

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_02.api_joke2.requests")
    def test_0124_get_joke2(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke2(), {"joke": "Hello World"})
        # self.assertEqual(mock_response.status_code , 200)

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_02.api_joke2.requests")
    def test_0125_fail_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke2(), "NO_JOKE NOT 200")
        # self.assertEqual(mock_response.status_code , 200)

    @pytest.mark.joke_mocks
    @patch("src.joke_mock_02.api_joke2.requests")
    def test_0126_get_joke_timeout_exception(self, mock_requests):
        """mocking requests"""
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effecct = Timeout("Seems that the server is down.")
        self.assertEqual(get_joke2(), "NO_JOKE NOT 200")
        # self.assertEqual(mock_response.status_code , 200)
