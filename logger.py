from loguru import logger

logger.add("errors.log", level="ERROR")

def log_error(error_message):
    logger.error(error_message)
