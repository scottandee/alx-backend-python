#!/usr/bin/env python3
"""This script contanins a function that uses
asynchronous comprehension to collect 10 numbers
from an asynchronous generator function
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function collects ten numbers from the
    `async_generator` function creates a list using
    async comprehension
    """
    return [i async for i in async_generator()]
