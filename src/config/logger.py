import os
import logging

from . import app_settings

def configure_logging():
    os.makedirs(app_settings.LOG_DIR, exist_ok=True)
    log_filename = f"{app_settings.LOG_DIR}/vitalia_core_api.log"

    log_level = logging.DEBUG if app_settings.DEBUG else logging.info
