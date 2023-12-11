#!/usr/bin/env python3
""" The `3-tasks` module supplies a function `task_wait_random` """
import asyncio
wait_random = __import__('3-tasks').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random: Function taking 1 arg `max_delay`
                      and returns a newly created task

    Args:
    max_delay:        int

    Return:
    new Task:         asyncio.Task
    """
    new_task = asyncio.create_task(wait_random(max_delay))
    return (new_task)
