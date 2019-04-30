import pathlib
import sys
from aiohttp import web
from src.app.main import initApp
from src.configs.appConfig import config
from src.app.logger.Logger import logger

BASE_DIR = pathlib.Path(__file__).parent
sys.path.append(BASE_DIR.as_posix())


filePathPrefix = config["filePathPrefix"]
dirs = config["fileDirs"]

for dir in dirs:
    path = pathlib.Path(f"{filePathPrefix}/{dir}")
    if not path.exists():
        logger.info(f"mkdir: {path.as_posix()}")
        path.mkdir(parents=True)

app = initApp()

web.run_app(app)
