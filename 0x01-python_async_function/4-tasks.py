#!/usr/bin/env python3
"""This script contains a function that
executes multiple coroutines
"""

from typing import List, Callable
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function spawns `task_wait_random` `n` times
    with the specified maximum delay
    """
    delays: List[float] = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n))
    )
    return sorted(delays)
