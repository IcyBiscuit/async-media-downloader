import aiofiles


async def saveFile(filename: str, data: bytes):
    '''
    异步保存文件
    :param filename: 待保存的文件的全路径文件名
    :param data: 文件数据流
    '''
    async with aiofiles.open(filename, mode='wb') as file:
        await file.write(data)
        await file.flush()
