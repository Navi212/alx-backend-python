#!/usr/bin/env python3
""" The `4-tasks` module supplies a function `task_wait_n` """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n: Function taking 2 args `n` and `max_delay`
                 and returns a list of delays

    Args:
    n:          int
    max_delay:  int

    Return:
    List of delays
    """

    delay_list = []

    for _ in range(n):
        delay_time = await task_wait_random(max_delay)
        delay_list.append(delay_time)

    return (delay_list)
