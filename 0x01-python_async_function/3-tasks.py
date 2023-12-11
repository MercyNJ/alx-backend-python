#!/usr/bin/env python3
"""
Module that Creates and returns an asyncio.Task
for wait_random with the specified max_delay.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a asyncio.Task
    """

    return asyncio.create_task(wait_random(max_delay))


