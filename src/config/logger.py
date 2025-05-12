import os
from . import app_settings

def configure_logging():
    os.makedirs(app_settings.LOG_DIR, exist_ok=True)
    log_filename = f"{app_settings.LOG_DIR}/vitalia_core_api.log"

    login_level 