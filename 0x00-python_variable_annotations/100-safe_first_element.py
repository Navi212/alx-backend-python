#!/usr/bin/env python3
"""
The `100-safe_first_element` module supplies a function
`safe_first_element`
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element: Function that takes a sequence like list,
                        tuples, strings

    Args:
    lst:                Sequence of Any type

    Return:             Data of Any type or None
    """
    if lst:
        return lst[0]
    else:
        return None
