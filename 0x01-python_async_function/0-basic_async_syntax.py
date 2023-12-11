#!/usr/bin/env python3
""" The `0-basic_async_syntax` module supplies a function `wait_random` """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: Function that takes max_delay arg
                 and returns a float

    Args:
    max_delay:   int

    Return:
    Float
    """
    rand_num = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return (rand_num)
