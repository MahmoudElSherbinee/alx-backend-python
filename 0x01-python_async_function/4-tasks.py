#!/usr/bin/env python3

"""
Tasks 4
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio
from typing import List
# wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This Funcition returns a lists of delays """
    # wait = await wait_random(max_delay)
    task = []
    wait = []

    for i in range(n):
        # tasks = wait_random(max_delay)
        tasks = task_wait_random(max_delay)
        task.append(tasks)

    for tasks in asyncio.as_completed((task)):
        delay = await tasks
        wait.append(delay)

    return wait
