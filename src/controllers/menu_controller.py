# Lógica para manejar las funciones simples del menú
from rich import print
from questionary import text, password, confirm
from src.services.auth import user_auth
from src.utils.file_helpers import read_json, write_json
from src.config.settings import USERS_JSON
from src.services.matcher import match_preferences
import time


def check_preferences():
    print("[bold]Ingresa tu usuario y contraseña para ver tus recomendaciones personalizadas.")
    user = user_auth()

    read_users = read_json(USERS_JSON)
    read_users = [u for u in read_users if u["username"] == user["username"]]
    print(f"¡Genial, {read_users[0]["data"]["name"]}! Vamos a revisar tus elecciones antes de mostrarte tus recomendaciones 🌱.")

    print("[bold]⏰ Rutina diaria:[/bold] " + read_users[0]["data"]["daily_routine"])
    print("[bold]🥗 Dieta:[/bold] " + read_users[0]["data"]["diet"])
    print("[bold]♿️ Movilidad reducida:[/bold] " + read_users[0]["data"]["disability"])
    print("[bold]🌿 Estilo de vida:[/bold] " + read_users[0]["data"]["lifestyle"])
    print("[bold]🚧 Obstáculos:[/bold] " + ", ".join(read_users[0]["data"]["obstacles"]))
    print("[bold]💪 Actividad física:[/bold] " + read_users[0]["data"]["physical_activity"])
    print("[bold]🚫 Restricciones:[/bold] " + ", ".join(read_users[0]["data"]["restrictions"]))
    print("[bold]💤 Sueño:[/bold] " + read_users[0]["data"]["sleep_quality"])
    print("[bold]🧠 Estrés:[/bold] " + read_users[0]["data"]["stress_level"])
    print("[bold]🎯 Metas de bienestar:[/bold] " + ", ".join(read_users[0]["data"]["wellbeing_goals"]))

    match_preferences(user)
    time.sleep(20)

def change_user():
    print("[bold]Ingresa tu usuario y contraseña para actualizar tu información.")
    user = user_auth()
    print("¡Hola de nuevo! Ya puedes actualizar tu información.")

    while True:
        new_username = text("Nuevo nombre de usuario: ").ask()

        if new_username:
            if new_username.isalnum():
                read_users = read_json(USERS_JSON)

                if any(user["username"] == new_username.lower() for user in read_users):
                    print(
                        "[bold red]El nombre de usuario que intentaste ingresar ya está en uso.")
                    continue
                break

            print(
                "[bold red]Tu nombre de usuario solo puede estar compuesto por letras y números, intentalo de nuevo.")
            continue
        break

    while True:
        new_password = password("Nueva contraseña: ").ask()

        if new_password:
            if new_password and len(new_password) > 7:
                break

            print(
                "[bold red]Tu contraseña debe tener al menos 8 caracteres, intentalo de nuevo.")
            continue
        break

    if new_username and new_password:
        for u in read_users:
            if u["username"] == user["username"]:
                u["username"] = new_username
                u["password"] = new_password
                write_json(USERS_JSON, read_users)
                break
    elif new_username and not new_password:
        for u in read_users:
            if u["username"] == user["username"]:
                u["username"] = new_username
                write_json(USERS_JSON, read_users)
                break
    elif not new_username and new_password:
        for u in read_users:
            if u["username"] == user["username"]:
                u["password"] = new_password
                write_json(USERS_JSON, read_users)
                break
    else:
        pass


def delete_user():
    print("[bold]Ingresa tu usuario y contraseña para eliminar tu cuenta.")
    user = user_auth()

    answer_is_yes = confirm(
        "¿Estás seguro/a de que quieres eliminar tu cuenta?").ask()
    if answer_is_yes:
        read_users = read_json(USERS_JSON)
        read_users = [u for u in read_users if u["username"]
                      != user["username"]]
        write_json(USERS_JSON, read_users)
        print("[bold green]Tu cuenta fue eliminada correctamente. ✅ ")
        time.sleep(3)
    else:
        pass
