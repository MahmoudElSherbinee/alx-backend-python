#!/usr/bin/env python3
import asyncio

async def fetch_data(delay, id):
    print(f"fetching data for {id}")
    await asyncio.sleep(delay)
    return f"Data for {id} fetched completely"


async def main():
    task1 = asyncio.create_task(fetch_data(2, 1))
    task2 = asyncio.create_task(fetch_data(3, 2))
    task3 = asyncio.create_task(fetch_data(1, 3))

    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1)
    print(result2)
    print(result3)

asyncio.run(main())