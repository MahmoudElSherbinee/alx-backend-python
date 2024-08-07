#!/usr/bin/env python3
""" This is a Asyncronious Program """


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This function takes no argument but loop 10 times
    to provide Asyncronious """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
