#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension coroutine.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous Comprehension Coroutine: Collects 10 random numbers
    using an asynchronous comprehension over async_generator.
    """

    output = [i async for i in async_generator()]
    return output
