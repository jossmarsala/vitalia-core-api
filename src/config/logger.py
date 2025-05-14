import os
import logging
from logging.handlers import TimedRotatingFileHandler

from . import app_settings

LOG_FORMAT= "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d"
DATETIMEFORMAR =  "%Y-%m-%d %H:%M:%S"

def configure_logging():
    os.makedirs(app_settings.LOG_DIR, exist_ok=True)
    log_filename = f"{app_settings.LOG_DIR}/vitalia_core_api.log"

    log_level = logging.DEBUG if app_settings.DEBUG else logging.INFO

    file_handler = TimedRotatingFileHandler(log_filename, "midnight", 1)
    file_handler.suffix = "%Y-%m-%d"

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter()
    console_handler.setFormatter