from aiohttp import web
import json
from calc import test_calc
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        # html = await fetch(session, 'http://localhost:8080/user?name=test')
        # print(html)
        session.post(session, 'http://localhost:8080/get')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())