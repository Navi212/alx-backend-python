#!/usr/bin/env python3
""" The `8-make_multiplier` module supplies a function `make_multiplier` """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: Function that takes arg `multiplier` and returns
                     a function that returns a float

    Args:
    multiplier: float

    Return:
    multiplier_fun: Function that returns float
    """
    def multiplier_fun(arg: float) -> float:
        """
        multiplier_fun: Function that multiplies arg `arg`, `multiplier`
                        arg of `make_multiplier` outter function and returns
                        the final value

        Args:
        arg: float

        Return:
        value: float
        """
        return (arg * multiplier)
    return (multiplier_fun)
