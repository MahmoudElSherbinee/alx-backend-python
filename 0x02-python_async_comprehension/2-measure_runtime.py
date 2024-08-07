#!/usr/bin/env python3
""" This file measures the runtime of an async function
"""


import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ This functio execute and """
    start_time = time.time()
    # for i in range(4):
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()

    run_time = end_time - start_time
    return run_time
