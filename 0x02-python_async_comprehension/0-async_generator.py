#!/usr/bin/env python3
"""This script contains the declaration of
an asynchronous generator function
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """This is an asychronous generator function
    that yields 10 values"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
