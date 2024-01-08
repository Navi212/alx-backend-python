#!/usr/bin/env python3
""" The `test_utils` supplies a class `TestAccessNestedMap` """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """  TestAccessNestedMap a test class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """ A test method """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_value)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_val):
        """ A test method implementing test with assertRaises """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ A test class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        A test method that mocks request-response object
        and sends the return value for response
        """
        response_mock = Mock()
        response_mock.json.return_value = test_payload
        with patch("utils.requests.get", return_value=response_mock):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ A test class that implements memoization """
    def test_memoize(self):
        """ A test method that implements memoization """
        class TestClass:
            """ A test class """

            def a_method(self):
                """ A that returns a value """
                return 42

            @memoize
            def a_property(self):
                """ A method that returns a method """
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, "a_method") as mock_obj:
            mock_obj.return_value = 42
            call_1 = test_obj.a_property
            call_2 = test_obj.a_property
            self.assertEqual(call_1, 42)
            self.assertEqual(call_2, 42)
            mock_obj.assert_called_once()
