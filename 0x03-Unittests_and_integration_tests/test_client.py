#!/usr/bin/env python3
"""
Test Client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    This class contains tests for the
    GithubOrgClient class
    """
    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        This method tests the org method of
        the GithubOrgClient class
        """
        expected_value = {"org": org_name}
        mock_get_json.return_value = expected_value

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_value)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == "__main__":
    unittest.main()
