import logging
import time
from src.configs.appConfig import config

import pathlib


def initLogger():
    logPath = pathlib.Path(config["logPath"])
    if not logPath.exists():
        logPath.mkdir(parents=True)

    dateFormat = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    logFilename = f"{logPath.as_posix()}/{dateFormat}.log"

    logFormatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    fileHandler = logging.FileHandler(logFilename)
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(logFormatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(logFormatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)

    return logger


logger = initLogger()
