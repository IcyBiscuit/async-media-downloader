from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from src.app.handlers.PocketHandler import routers
import src.app.handlers.PocketHandler as pocketHandler

from src.app.logger.Logger import logger


class Test(AioHTTPTestCase):
    async def get_application(self):
        """
        Override the get_app method to return your application.
        """

        app = web.Application()
        app.router.add_routes(routers)
        return app

    @unittest_run_loop
    async def image(self):
        resp = await self.client.request("POST", "/downloadImage")
        print(resp)

    def testImage(self):
        async def image():
            resp = await self.client.request("POST", "/downloadImage", data={
                "url": "https://nim.nosdn.127.net/NDA5MzEwOA==/bmltYV83MjUyMDE5NDYwXzE1NTU0Mjg5OTU1MDZfYjhjNzI3N2UtZjM4OC00YzA2LWE5NzMtYzM1YTQ5OWUyMDhl"
            })
            # logger.debug(req)
            # resp = await pocketHandler.downloadImage(req)
            logger.debug(resp)
            print(await resp.json())
        self.loop.run_until_complete(image())

    def testAudio(self):
        async def audio():
            resp = await self.client.request("POST", "/downloadAudio", data={
                "url": "https://nim.nosdn.127.net/NDA5MzEwOA==/bmltYV83MjUyMDE5NDYwXzE1NTU0Mjg5OTU1MDZfYjhjNzI3N2UtZjM4OC00YzA2LWE5NzMtYzM1YTQ5OWUyMDhl"
            })
            logger.debug(resp)
            print(await resp.json())
        self.loop.run_until_complete(audio())

    def testGif(self):
        async def gif():
            resp = await self.client.request("POST", "/downloadGif", data={
                "url": "https://nim.nosdn.127.net/NDA5MzEwOA==/bmltYV83MjUyMDE5NDYwXzE1NTU0Mjg5OTU1MDZfYjhjNzI3N2UtZjM4OC00YzA2LWE5NzMtYzM1YTQ5OWUyMDhl"
            })
            logger.debug(resp)
            print(await resp.json())
        self.loop.run_until_complete(gif())

    def testSession(self):
        async def session():
            # clientSession = await pocketHandler.getSession()
            clientSession = pocketHandler.clientSession
            print(clientSession)
        self.loop.run_until_complete(session())
