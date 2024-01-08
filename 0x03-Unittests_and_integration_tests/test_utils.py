#!/usr/bin/env python3
""" The `test_utils` supplies a class `TestAccessNestedMap` """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """  TestAccessNestedMap a test class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """ A test method """
        assertEqual(access_nested_map(nested_map, path), expected_value)
