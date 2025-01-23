#Implement a custom logger module and use it to log messages to a file.
import logging
from datetime import datetime
def setup_logger(log_file="app.log", level=logging.INFO):
    logger = logging.getLogger("CustomLogger")
    logger.setLevel(level)
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
