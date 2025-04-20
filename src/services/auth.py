# Lógica para la autenticación del usuario

from src.utils.file_helpers import read_json
from src.config.settings import USERS_JSON  
from src.models.user import UserModel
from questionary import text, password
from rich import print

def user_auth() -> dict:
    while True:
        username_login = text("Nombre de usuario: ").ask()

        if username_login:
            read_users = read_json(USERS_JSON)

            if any(user["username"] == username_login.lower() for user in read_users):
                user = next((u for u in read_users if u["username"] == username_login.lower()), None)
                break
            else:
                print("[bold red]El usuario que intentaste ingresar no existe.")
                continue

        print("[bold red]Este campo es obligatorio.")
        continue

    while True:
        password_login = password("Contraseña: ").ask()

        if password_login:
            read_user_pwd = read_json(USERS_JSON)

            if any(username_login in d.values() and password_login in d.values() for d in read_user_pwd):
                return UserModel(**user)
            else:
                print("[bold red]Contraseña incorrecta, intentalo de nuevo.")
                continue

        print("[bold red]Este campo es obligatorio.")
        continue
