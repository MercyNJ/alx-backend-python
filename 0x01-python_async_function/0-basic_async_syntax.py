#!/usr/bin/env python3
"""
Module demonstrating basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds (float)
    and eventually returns it.
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
