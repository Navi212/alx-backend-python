#!/usr/bin/env python3
"""
The `2-measure_runtime` module supplies a function
`measure_runtime`
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime: Function taking no arg and returning float

    Args:
    None

    Return:
    Float
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    stop_time = time()
    elapsed_time = stop_time - start_time
    return elapsed_time
