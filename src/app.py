from src.utils.cli_helpers import clear_console
from src.controllers.user_controller import create_user
from src.controllers.menu_controller import change_user, check_preferences, delete_user

from rich import print
from questionary import select, confirm


def run_app():

    clear_console()

    while True:
        clear_console()
        print("[bold]¡Bienvenido/a a Wellness Matcher 🧘🌱! \n")

        option = select(
            "¿Qué quieres hacer hoy?",
            choices=[
                "1. Registrarme (crear usuario)",
                "2. Ver recomendaciones",
                "3. Actualizar mi nombre de usuario",
                "4. Eliminar usuario",
                "🚪 Salir"
            ]
        ).ask()

        match option:
            case "1. Registrarme (crear usuario)":
                create_user()
            case "2. Ver recomendaciones":
                check_preferences()
            case "3. Actualizar mi nombre de usuario":
                change_user()
            case "4. Eliminar usuario":
                delete_user()
            case "🚪 Salir":
                answer_is_yes = confirm("¿Estás seguro/a de que quieres salir?").ask()

                if answer_is_yes:
                    print("¡Nos vemos pronto 👋!")
                    break
                else:
                    continue 


 