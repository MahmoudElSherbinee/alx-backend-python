#!/usr/bin/env python3
"""
Asyncio and Random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay: int
    Returns:
        float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
