# Download all comments from a subreddit of your choice using URL:
# https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump them to a file.
# For this task use asyncio and aiohttp libraries for making requests to Reddit API.

import asyncio
import json
import time
from aiohttp import ClientSession


async def get_comments():
    async with ClientSession() as session:
        url = f'https://api.pushshift.io/reddit/comment/search/'

        async with session.get(url=url) as response:
            comment_json = await response.json()
            return f'{comment_json}'


async def main():
    tasks = []
    tasks.append(asyncio.create_task(get_comments()))

    results = await asyncio.gather(*tasks)

    with open('f.json', 'w') as f:
        json.dump(results,f)
    print(type(results[0]))
    # for result in results:
    #     print(result)


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))