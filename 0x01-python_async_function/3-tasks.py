#!/usr/bin/env python3
"""
Tasks 3
Write a function (do not create an async function,
use the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task.

"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Args:
        max_delay: int
    Returns:
        asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
