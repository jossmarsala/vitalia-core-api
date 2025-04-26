# Funciones auxiliares para la aplicación 

from src.utils.file_helpers import read_json, write_json
from src.config.settings import USERS_JSON
from src.models.temp_user import TempUserModel
from src.services.matcher import match_preferences

def save_user(user: dict):
    users = read_json(USERS_JSON)
    users.append(user)
    
    write_json(USERS_JSON, users)

def test_temp_user():
    fake_user = TempUserModel()
    match_preferences(fake_user)
    print(fake_user.data)

