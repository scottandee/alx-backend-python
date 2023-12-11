#!/usr/bin/env python3
"""This script contains basic async syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function waits for a random delay
    between 0 and `max_delay` seconds and eventually
    returns it
    """
    n: float = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
