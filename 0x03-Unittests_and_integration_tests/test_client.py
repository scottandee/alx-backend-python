#!/usr/bin/env python3
"""Test Client
"""

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url
        is the expected one
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            org_name = "google"
            url = f"https://www.{org_name}.com"
            mock_org.return_value = {"repos_url": url}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, url)
