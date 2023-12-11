#!/usr/bin/env python3
""" The `2-measure_runtime` module supplies a function `measure_time` """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time:     Function taking 2 args `n` and `max_delay`
                      and returns a measure time (float)

    Args:
    n:                int
    max_delay:        int

    Return:
    measure time:     float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed = end_time - start_time

    return (elapsed / n)
