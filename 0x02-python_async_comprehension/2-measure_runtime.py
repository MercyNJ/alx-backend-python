#!/usr/bin/env python3
"""Module import async_comprehension from the previous file and
contains a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""


import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime"""
    start = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time.time()
    return (end - start)
