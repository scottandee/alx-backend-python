#!/usr/bin/env python3
"""Test Client
"""

import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """This class contains tests for the
    GithubOrgClient class
    """
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, test_org_name, mock_get_json):
        """Test that GithubOrgClient.org returns
        the correct value
        """
        mock_get_json.return_value = {"test_key": test_org_name}
        client = GithubOrgClient(test_org_name)
        self.assertEqual(client.org, {"test_key": test_org_name})
