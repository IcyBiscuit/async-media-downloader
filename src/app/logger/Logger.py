import logging
import time
from src.configs.appConfig import config

import pathlib


def initLogger():
    logPath = pathlib.Path(config["logPath"])
    if not logPath.exists():
        logPath.mkdir(parents=True)

    dateFormat = time.strftime("'%Y-%m-%d", time.localtime(time.time()))
    logFilename = f"log/{dateFormat}.log"

    logFormatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    fileHandler = logging.FileHandler(logFilename, mode="w")
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(logFormatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logFormatter)

    logger = logging.getLogger()
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger


logger = initLogger()
