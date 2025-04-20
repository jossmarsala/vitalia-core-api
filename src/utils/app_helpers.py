# Funciones auxiliares para la aplicación 

from src.utils.file_helpers import read_json, write_json
from src.config.settings import USERS_JSON

def save_user(user: dict):
    users = read_json(USERS_JSON)
    users.append(user)
    
    write_json(USERS_JSON, users)