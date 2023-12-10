#!/usr/bin/env python3
"""
The `101-safely_get_value` module supplies a function
`safely_get_value`
"""
from typing import Mapping, TypeVar, Callable, Any, Union


"""Describes a custom typevariable"""
T = TypeVar('T')
default = Union[T, None]
ret_val = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: default) -> ret_val:
    """
    safely_get_value: Function that accepts a dictionary(Mapping),
                      Key(Type:Any), default(Type: T(typevar or None))
                      as arguments and returns Any or T

    Args:
    dct:              Mapping
    key:              Any
    default:          T or None

    Return:
    Type:             Any or T
    """
    if key in dct:
        return dct[key]
    else:
        return default
