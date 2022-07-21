#Creation of web server

from aiohttp import web

# step 1 : Create request handler
# Request Handler : It is code routine - accepts only 1 param - request 
#                   returns Response object

async def get_handler(request):
    return web.Response(text = "Hi Vaishnavi")

# step 2 : Creating application instance

app = web.Application()

# step 3 : Adding path to handler / registering the request handler to http method

app.add_routes([web.get('/', get_handler)])

web.run_app(app)