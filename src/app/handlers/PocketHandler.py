import asyncio
import uuid

from aiohttp import ClientSession, ClientTimeout, TCPConnector, web

from src.configs.appConfig import config

filePrefix = config["filePathPrefix"]
routers = web.RouteTableDef()


clientSession = asyncio.get_event_loop().run_until_complete(getSession())


@routers.post(path="/downloadImage")
async def downloadImage(requests):
    data = await requests.post()
    if "url" not in data:
        return
    imgUrl = data["url"]

    filename = uuid.uuid1().hex
    jsonResp = {
        "path": f"{filePrefix}/{filename}.jpg"
    }

    return web.json_response(jsonResp)


async def getSession():
    return await ClientSession(timeout=ClientTimeout(30), connector=TCPConnector(ssl=False))
