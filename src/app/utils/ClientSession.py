import aiohttp

clientSession=None

async def getSession():
    clientSession=aiohttp