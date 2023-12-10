#!/usr/bin/env python3
""" The `6-sum_mixed_list` module supplies a function `mxd_lst` """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: Function that takes a list of ints and floats
                    and returns their sum as float

    Args:
    mxd_lst: list of ints and floats

    Return:
    sum: float
    """
    return (float(sum(mxd_lst)))
