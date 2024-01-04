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
    def test_access_nested_map_successful_cases(
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
    def test_access_nested_map_exception_cases(
            self, nested_map, path, expected_exception):
        """Test access_nested_map for exception cases.

        Parameters:
        - nested_map (dict): The nested map to be tested.
        - path (tuple): The path to access within the nested map.
        - expected_exception (type): The expected exception type to be raised.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
