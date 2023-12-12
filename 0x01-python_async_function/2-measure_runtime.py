#!/usr/bin/env python3
"""This script contains a function that measures
the runtime of the `wait_n` function
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This function measures the total execution time
    for the `wait_n` function
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
