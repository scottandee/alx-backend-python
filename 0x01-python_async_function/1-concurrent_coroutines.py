#!/usr/bin/env python3
"""This script contains a function that
executes multiple coroutines
"""

from typing import List, Callable
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function spawns `wait_random` `n` times
    with the specified maximum delay
    """
    delays: List[float] = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n))
    )
    return sorted(delays)
