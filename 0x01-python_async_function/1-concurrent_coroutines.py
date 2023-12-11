#!/usr/bin/env python3
""" The `1-concurrent_coroutines` module supplies a function `wait_n` """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n:     Function taking 2 args `n` and `max_delay`
                and returns a list of delays

    Args:
    n:          int
    max_delay:  int

    Return:
    List of delays
    """
    delay_list = []

    for i in range(n):
        delay_time = await wait_random(max_delay)
        delay_list.append(delay_time)

    return (delay_list)
