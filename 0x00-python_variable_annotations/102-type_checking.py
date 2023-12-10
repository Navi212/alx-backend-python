#!/usr/bin/env python3
""" The `102-type_checking.py` module supplies a function `zoom_array` """
from typing import Tuple, Iterable, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom_array: Function taking args Tuple and int and returns a List

    Args:
    lst:        Tuple
    factor:     int

    Return:
    List:       List
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
