#!/usr/bin/env python3
"""This script contains a function that runs
async comprehensions concurrently and measures
the runtime
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function maeasures the runtime of four
    concurent list comprehensions
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end: float = time.perf_counter()
    return end - start
