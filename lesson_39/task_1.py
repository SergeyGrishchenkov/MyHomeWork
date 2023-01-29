# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
# Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10.
# You need to get four lists of results from corresponding functions.
# Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
# Time the execution of both realizations, explore the results, what realization is more effective,
# why did you get a result like this.

import asyncio
import time

async def sq():
    l = []
    n = int(input())
    for item in range(n + 1):
        l.append(item ** 2)
    return l

async def cubic():
    l = []
    n = int(input())
    for item in range(n + 1):
        l.append(item ** 3)
    return l


async def main():
    tasks = []
    tasks.append(sq())
    tasks.append(cubic())

    result = await asyncio.gather(*tasks)
    print(result)


if __name__ == '__main__':
    asyncio.run(main())