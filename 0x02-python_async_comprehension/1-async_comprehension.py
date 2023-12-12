#!/usr/bin/env python3
"""
The `1-async_comprehension` module supplies a function
`async_comprehension`
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension: Function  taking no arg and returns
                         List of floats

    Args:
    None

    Return:
    List of floats
    """
    return [i async for i in async_generator()]
