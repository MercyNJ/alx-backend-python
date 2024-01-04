#!/usr/bin/env python3
""" Module for testing client module """

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test class for the GithubOrgClient."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    def test_org(self, org: str, expected_response: dict):
        """Test the org method of GithubOrgClient."""
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = MagicMock(
                    return_value=expected_response)

            goclient = GithubOrgClient(org)
            result = goclient.org()

            expected_url = f"https://api.github.com/orgs/{org}"
            mock_get_json.assert_called_once_with(expected_url)

            self.assertEqual(result, expected_response)

    def test_public_repos_url(self):
        """Test the _public_repos_url property of GithubOrgClient."""
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = \
                    {"repos_url": "https://api.github.com/orgs/testorg/repos"}
            goclient = GithubOrgClient("testorg")
            result = goclient._public_repos_url
            expected_url = "https://api.github.com/orgs/testorg/repos"
            self.assertEqual(result, expected_url)
