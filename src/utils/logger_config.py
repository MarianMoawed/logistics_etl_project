
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config.config import LOG_FILE_PATH


LOG_DIR = os.path.dirname(LOG_FILE_PATH)

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("LogisticsPipelineLogger")
logger.setLevel(logging.INFO)

file_handler = TimedRotatingFileHandler(
    LOG_FILE_PATH, 
    when="midnight",
    interval=1, 
    backupCount=30)
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)