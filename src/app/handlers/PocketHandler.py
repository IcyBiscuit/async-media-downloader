from aiohttp import web
import uuid

from src.configs.appConfig import config

filePrefix = config["filePathPrefix"]
routers = web.RouteTableDef()


@routers.post(path="/downloadImage")
async def downloadImage(requests):
    data = await requests.json()

    if "url" not in data:
        return

    filename = uuid.uuid1().hex
    jsonResp = {
        "path": f"{filePrefix}/{filename}.jpg"
    }

    return web.json_response(jsonResp)
