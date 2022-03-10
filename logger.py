import os
import sys
from datetime import timedelta

from loguru import logger
from loguru._defaults import LOGURU_TRACE_NO


def setup_logger():
    file_path = "./logs"

    try:
        os.makedirs(file_path, exist_ok=True)
    except FileNotFoundError:
        pass  # if passed file path consist only filename

    logger.remove()
    log_format = "[{time:YYYY-MM-DD HH:mm:ss ZZ}] [{process}] [{level}] [{name}] {message}"

    logger.add(
        sink=sys.stdout,
        level=LOGURU_TRACE_NO,
        format=log_format
    )
    # logger.add(
    #     sink=file_path,
    #     level=LOGURU_TRACE_NO,
    #     format=log_format,
    #     rotation=timedelta(days=1),
    #     retention=timedelta(days=7)
    # )
