from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, make_mocked_request

from src.app.handlers.PocketHandler import routers
import src.app.handlers.PocketHandler as pocketHandler


class Test(AioHTTPTestCase):
    async def get_application(self):
        """
        Override the get_app method to return your application.
        """

        app = web.Application()
        app.router.add_routes(routers)
        return app

    # @unittest_run_loop
    # async def image(self):
    #     resp = await self.client.request("POST", "/downloadImage")
    #     print(resp)

    def testImage(self):
        async def image():
            # req = make_mocked_request(
            #     method="POST", path="/downloadImage",payload={
            #     },)
            resp = await self.client.request("POST", "/downloadImage")
            print(await resp.json())
        self.loop.run_until_complete(image())

    def sessionTest(self):
        async def session():
            clientSession = await pocketHandler.getSession()
            print(clientSession)
        self.loop.run_until_complete(session)
