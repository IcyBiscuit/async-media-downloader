from src.app.handlers.PocketHandler import routers

from aiohttp import web


def initApp():
    app = web.Application()
    app.add_routes(routers)
    return app
