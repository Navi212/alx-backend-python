#!/usr/bin/env python3
""" The `5-sum_list` module supplies a funcion `sum_list` """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list: Function that returns sum of floats in the list

    Args:
    input_list: List of floats

    Return:
    sum: float
    """
    return (float(sum(input_list)))
