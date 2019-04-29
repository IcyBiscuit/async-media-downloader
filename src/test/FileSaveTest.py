from src.app.utils.SaveFileAsync import saveFile
import asyncio


file = open('src/temp/test.jpg', 'rb')

data = file.read()

task = asyncio.ensure_future(saveFile('src/temp/out/test.jpg', data))

loop = asyncio.get_event_loop()

loop.run_until_complete(task)
