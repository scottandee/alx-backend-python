#!/usr/bin/env python3
"""Test Utils
"""

import unittest
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json
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
