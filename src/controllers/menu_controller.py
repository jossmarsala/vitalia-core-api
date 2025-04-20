# Lógica para manejar las funciones simples del menú

from rich import print
from questionary import text, password, confirm
from src.services.auth import user_auth
from src.utils.file_helpers import read_json, write_json
from src.config.settings import USERS_JSON
from src.models.user import UserModel
from src.services.matcher import match_preferences
import time

class MenuController:
    def check_preferences(self):
        print("\n Ingresa tu usuario y contraseña para ver tus recomendaciones personalizadas.")
        user = user_auth()

        read_users = read_json(USERS_JSON)
        read_users = [u for u in read_users if u["username"] == user["username"]]
        print(f"\n¡Genial, {user.data['name']}! Vamos a revisar tus elecciones antes de mostrarte tus recomendaciones.\n")

        print("[bold]⏰ Rutina diaria:[/bold] " + user.data["daily_routine"])
        print("[bold]🥗 Dieta:[/bold] " + user.data["diet"])
        print("[bold]♿️ Movilidad reducida:[/bold] " + user.data["disability"])
        print("[bold]🌿 Estilo de vida:[/bold] " + user.data["lifestyle"])
        print("[bold]🚧 Obstáculos:[/bold] " + ", ".join(user.data["obstacles"]))
        print("[bold]💪 Actividad física:[/bold] " + user.data["physical_activity"])
        print("[bold]🚫 Restricciones:[/bold] " + ", ".join(user.data["restrictions"]))
        print("[bold]💤 Sueño:[/bold] " + user.data["sleep_quality"])
        print("[bold]🧠 Estrés:[/bold] " + user.data["stress_level"])
        print("[bold]🎯 Metas de bienestar:[/bold] " + ", ".join(user.data["wellbeing_goals"]))

        match_preferences(user)


    def change_user(self):
        print("\n Ingresa tu usuario y contraseña para actualizar tu información.")
        user = user_auth()
        print("\n¡Hola de nuevo! Ya puedes actualizar tu información.")

        read_users = [UserModel(**u) for u in read_json(USERS_JSON)]

        while True:
            new_username = text("Nuevo nombre de usuario: ").ask()

            if new_username:
                if new_username.isalnum():
                    if any(u.username == new_username.lower() for u in read_users):
                        print("[bold red]El nombre de usuario que intentaste ingresar ya está en uso.")
                        continue
                    break

                print("[bold red]Tu nombre de usuario solo puede estar compuesto por letras y números, intentalo de nuevo.")
                continue
            break

        while True:
            new_password = password("Nueva contraseña: ").ask()

            if new_password:
                if len(new_password) > 7:
                    break

                print("[bold red]Tu contraseña debe tener al menos 8 caracteres, intentalo de nuevo.")
                continue
            break

        if new_username and new_password:
            for u in read_users:
                if u.username == user.username:
                    u.username = new_username.lower()
                    u.password = new_password
                    write_json(USERS_JSON, [usr.to_dict() for usr in read_users])
                    break

        elif new_username and not new_password:
            for u in read_users:
                if u.username == user.username:
                    u.username = new_username.lower()
                    write_json(USERS_JSON, [usr.to_dict() for usr in read_users])
                    break

        elif not new_username and new_password:
            for u in read_users:
                if u.username == user.username:
                    u.password = new_password
                    write_json(USERS_JSON, [usr.to_dict() for usr in read_users])
                    break
        else:
            pass

    def delete_user(self):
        print("Ingresa tu usuario y contraseña para eliminar tu cuenta.")
        user = user_auth()

        answer_is_yes = confirm(
            "¿Estás seguro/a de que quieres eliminar tu cuenta?").ask()
        if answer_is_yes:
            all_users = read_json(USERS_JSON)
            updated_users = [d for d in all_users if d["username"] != user.username]
            write_json(USERS_JSON, updated_users)
            print("[bold green]Tu cuenta fue eliminada correctamente. ✅[/bold green]")
            time.sleep(3)
        else:
            pass
