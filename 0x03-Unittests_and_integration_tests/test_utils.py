#!/usr/bin/env python3
"""Test Utils
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Any, Dict, Set, Callable


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
        ({"a": 1},("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """This tests the exception that is usually
        raised when incorrect inputs are passed into
        the function
        """
        self.assertRaises(KeyError)
