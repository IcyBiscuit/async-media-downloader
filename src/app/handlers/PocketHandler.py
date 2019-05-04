import uuid

from aiohttp import ClientSession, web

from src.app.logger.Logger import logger
from src.app.utils.SaveFileAsync import saveFile
from src.configs.appConfig import config

filePrefix = config["filePathPrefix"]
routers = web.RouteTableDef()


@routers.post(path="/downloadImage")
async def downloadImage(requests: web.Request):
    """
    下载静态图片处理流程
    """
    logger.debug(requests)
    data = await requests.post()
    if "url" not in data:
        return web.json_response({"msg": "缺少请求参数"})

    logger.debug(data["url"])
    imgUrl = data["url"]

    try:
        data = await getData(imgUrl)
        filename = f"{filePrefix}/img/{uuid.uuid1().hex}.jpg"
        await saveFile(filename, data)
        jsonResp = {
            "path": filename
        }
        return web.json_response(jsonResp)
    except IOError as err:
        logger.error(f"图片文件下载失败, url: {imgUrl}, err: {err}", exc_info=True)
        raise web.HTTPInternalServerError(body={
            "msg": "下载图片出错"
        })


@routers.post(path="/downloadGif")
async def downloadGif(requests: web.Request):
    """
    下载Gif图片处理流程
    """
    logger.debug(requests)
    data = await requests.post()
    if "url" not in data:
        return web.json_response({"msg": "缺少请求参数"})

    logger.debug(data["url"])
    imgUrl = data["url"]

    try:
        data = await getData(imgUrl)
        filename = f"{filePrefix}/img/{uuid.uuid1().hex}.gif"
        await saveFile(filename, data)
        jsonResp = {
            "path": filename
        }
        return web.json_response(jsonResp)
    except IOError as err:
        logger.error(f"gif图片文件下载失败, url: {imgUrl}, err: {err}", exc_info=True)
        raise web.HTTPInternalServerError(body={
            "msg": "下载gif图片出错"
        })


@routers.post(path="/downloadAudio")
async def downloadAudio(requests: web.Request):
    """
    下载语音文件处理流程
    """
    logger.debug(requests)
    data = await requests.post()
    if "url" not in data:
        return web.json_response({"msg": "缺少请求参数"})

    logger.debug(data["url"])
    audioUrl = data["url"]

    try:
        data = await getData(audioUrl)
        filename = f"{filePrefix}/audio/{uuid.uuid1().hex}.aac"
        await saveFile(filename, data)
        jsonResp = {
            "path": filename
        }
        return web.json_response(jsonResp)
    except IOError as err:
        logger.error(f"语音文件下载失败, url: {audioUrl}, err: {err}", exc_info=True)
        raise web.HTTPInternalServerError(body={
            "msg": "下载语音出错"
        })


async def getData(url: str):
    """
    通过url获取网络资源数据
    :param url: 网络资源所在url
    :returns: 资源的二进制数据
    """
    async with ClientSession() as session:
        async with session.get(url=url) as resp:
            return await resp.read()
