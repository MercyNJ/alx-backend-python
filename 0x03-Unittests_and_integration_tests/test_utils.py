#!/usr/bin/env python3
"""
Module that tests utils.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test case class for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map, path, expected_output):
        """Test access_nested_map for successful cases.

        Parameters:
        - nested_map (dict): The nested map to be tested.
        - path (tuple): The path to access within the nested map.
        - expected_output (any): The expected result of function.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception):
        """Test access_nested_map for exception cases.

        Parameters:
        - nested_map (dict): The nested map to be tested.
        - path (tuple): The path to access within the nested map.
        - expected_exception (type): The expected exception type to be raised.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, expected_payload):
        """Test get_json with parameterized inputs."""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = expected_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, expected_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """Test the memoize decorator functionality."""

        class TestClass:
            """Test class for memoization."""

            def a_method(self):
                """A sample method."""
                return 42

            @memoize
            def a_property(self):
                """A memoized property using the memoize decorator."""
                return self.a_method()

        test_instance = TestClass()
        with patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42
            res1 = test_instance.a_property
            res2 = test_instance.a_property
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
            mock_method.assert_called_once()
