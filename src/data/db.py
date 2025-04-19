# Funciones para leer y escribir JSON

from typing import List
from src.utils.file_helpers import read_json
from src.config.settings import USERS_JSON, RESOURCES_JSON
from src.models.user import UserModel

def initialize_data() -> List[UserModel]:
   user_list: list[dict] = read_json(USERS_JSON)
   return [UserModel(**user_dict) for user_dict in user_list]