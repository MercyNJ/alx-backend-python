#!/usr/bin/env python3
""" Module for testing client module """

from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    @patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_url, mock_get_json):
        """Test the public_repos method of GithubOrgClient."""
        mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload
        goclient = GithubOrgClient("testorg")
        result = goclient.public_repos()
        expected_repos = ["repo1", "repo2"]
        self.assertEqual(result, expected_repos)
        mock_url.assert_called_once()
        expected_url = "https://api.github.com/orgs/testorg/repos"
        mock_get_json.assert_called_once_with(expected_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test for GithubOrgClient.has_license."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Test the public_repos method."""
        result = GithubOrgClient("google").public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with the argument license='apache-2.0'."""
        result = GithubOrgClient("google").public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.get_patcher.stop()
