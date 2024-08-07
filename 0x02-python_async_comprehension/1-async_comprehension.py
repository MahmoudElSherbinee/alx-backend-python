#!/usr/bin/env python3
""" This file imports Import 'async_generator' from the previous
file to create a coroutine
"""

import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ This funtion generates a list of 10 """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
