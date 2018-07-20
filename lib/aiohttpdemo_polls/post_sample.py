from aiohttp import web
import aiohttp
import json
# import requests


url = 'http://localhost:8080'
files = {'file': open('../test_files/test.txt', 'rb')}


async def post_handler(request):
    return web.FileResponse('post', url, data=files)

app = web.Application()
app.router.add_get('/post', post_handler)
web.run_app(app)