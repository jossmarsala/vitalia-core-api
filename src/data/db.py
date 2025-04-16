# Funciones para leer y escribir JSON

from src.utils.file_helpers import read_json
from src.config.settings import USERS_JSON

def initialize_data() -> list[dict]:
    return read_json(USERS_JSON)
