# Funciones para leer y escribir JSON

from src.utils.file_helpers import read_json
from src.config.settings import USERS_JSON, RESOURCES_JSON

def initialize_data() -> list[dict]:
    return read_json()
