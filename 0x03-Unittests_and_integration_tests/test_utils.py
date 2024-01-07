#!/usr/bin/env pypython3
"""Test Utils
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Any, Dict, Set


class TestAccessNestedMap(unittest.TestCase):
    """This class tests the access nested map
    function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Set, expected_output: Any) -> None:
        """Test the access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)
