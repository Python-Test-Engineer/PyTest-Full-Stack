"""Test"""

import unittest

from .doubles import AppTestDouble
from .app import AppClient


class TestApp(unittest.TestCase):
    """Test"""

    def test_0115_get_ents_returns_dictionary_given_empty_string(
        self,
    ):
        """test"""
        model = "SOME_MODEL"
        ents = ""
        mock_obj = AppTestDouble(model)
        mock_obj.return_result(ents)
        ner = AppClient(mock_obj)
        result = ner.get_result("")
        self.assertIsInstance(result, dict)

    def test_0116_get_ents_returns_dictionary_given_non_empty_string(
        self,
    ):
        """test"""
        ents = "ENTITIES"
        model = "SOME_MODEL"
        mock_obj = AppTestDouble(model)
        mock_obj.return_result(ents)
        ner = AppClient(mock_obj)
        ents = ner.get_result("London is the capital of the UK")
        self.assertIsInstance(ents, dict)

    def test_0117_app_func_to_patch(self):
        """This is a test by patching main function in app.py"""
        model = "SOME_MODEL"
        # mock_obj = AppTestDouble(model)
        # mock_obj.return_result(ents)
        ner = AppClient(model)
        result = ner.func_to_patch()

        self.assertEqual(result, 20)
