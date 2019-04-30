import aiofiles
import aiofiles.os
import os

async def saveFile(filename, data):
    '''
    args:
        filename: 待保存的文件的全路径文件名
        data： 文件数据流
    '''
    async with aiofiles.open(filename, mode='wb') as file:
        await file.write(data)
        await file.flush()
