import logging
import os

def logGen():
    if not os.path.exists("./logs"):
        os.makedirs("./logs")
    logger = logging.getLogger("nopCommerce")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("./logs/automation.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger