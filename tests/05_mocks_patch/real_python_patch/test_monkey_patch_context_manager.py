import unittest
from real_python_patch import get_holidays, requests
from requests.exceptions import Timeout
from unittest.mock import patch


# autospec=True
# For ensuring that the mock objects in your tests have the same api as the objects they are replacing, you can use auto-speccing. Auto-speccing can be done through the autospec argument to patch, or the create_autospec() function. Auto-speccing creates mock objects that have the same attributes and methods as the objects they are replacing, and any functions and methods (including constructors) have the same call signature as the real object.
# https://docs.python.org/3/library/unittest.mock.html
# If the spec changes then if autospec=True an error will be thrown. Not so if set to False.


class TestRealPython(unittest.TestCase):
    def test_0134_get_holidays_timeout(self):
        with patch("real_python_patch.requests", autospec=True) as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

    def test_0135_get_holidays_timeout(self):
        with patch("real_python_patch.requests", autospec=True) as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


class TestRealPython2(unittest.TestCase):
    @patch.object(
        requests, "get", side_effect=requests.exceptions.Timeout, autospec=True
    )
    def test_0136_get_holidays_timeout(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()


if __name__ == "__main__":
    unittest.main()
