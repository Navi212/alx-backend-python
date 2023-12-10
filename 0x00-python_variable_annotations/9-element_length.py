#!/usr/bin/env python3
""" The `9-element_length` module supplies a function `element_length` """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: Function that takes iterable asa an argument
                    Example of an iterable, list, tuple etc that
                    permits the 'for loop construct'

    Args:
    lst:            Iterable of Sequence

    Return:
    List            A list of tuples. Tuples of [sequence and ints]
    """
    return [(i, len(i)) for i in lst]
