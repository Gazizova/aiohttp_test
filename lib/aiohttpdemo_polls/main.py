from aiohttp import web
import asyncio
import aiohttp
# from settings import config
import json

from aiohttp.web_app import Application
# from calc import test_calc

# app = web.Application()
# setup_routes(app)
# app['config'] = config
# web.run_app(app)

# 0 case
async def handle(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))
# 1st case
async def new_user(request):
    try:
        # happy path where name is set
        user = request.query['name']
        # Process our new user
        print("Creating new user with name: ", user)
        response_obj = {'status': 'success', 'message': 'user successfully created'}
        # return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        # Bad path where name is not set
        response_obj = {'status': 'failed', 'reason': str(e)}
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)

# 2nd case
routes = web.RouteTableDef()

@routes.get('/get')
async def get_handler(request):
       return web.Response(text='success')

# 3rd case:
@routes.post('/post')
async def post_handler(request):
    return web.FileResponse('../test_files/test.txt')


app = web.Application()
# call for 1st case
# app.router.add_post('/user', new_user)

# call for 2nd case:
# app.router.add_get('/', get_page)
app.add_routes(routes)

web.run_app(app)
