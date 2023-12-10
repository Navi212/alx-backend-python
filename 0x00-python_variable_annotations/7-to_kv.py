#!/usr/bin/env python3
""" The `7-to_kv` module supplies a function `to_kv` """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: Function that takes args `k` and `v` and
           returns a tuple

    Args:
    k: str
    v: int or float

    Return:
    tuple
    """
    square = float(v * v)
    return (k, square)
