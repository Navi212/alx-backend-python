#!/usr/bin/env python3
""" The `0-async_generator` module supplies a function `async_generator` """
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    async_generator: Function that takes no arg and returns
                     list of float

    Args:
    None

    Return:
    List of floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
