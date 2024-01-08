#!/usr/bin/env python3
"""Test Utils
"""

import unittest
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """This class tests the access nested map
    function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """This method tests the access nested
        map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """This tests the exception that is usually
        raised when incorrect inputs are passed into
        the function
        """
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """This class tests the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests):
        """This function tests the get_json function"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_requests.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """This class contains tests for the momoize
    function
    """
    def test_memoize(self):
        """This function tests the memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        instance = TestClass()
        with patch.object(instance, "a_method") as mocked_a_method:
            mocked_a_method.return_value = 42

            result_1 = instance.a_property
            result_2 = instance.a_property

            mocked_a_method.assert_called_once()
            self.assertEqual(result_1, result_2)
