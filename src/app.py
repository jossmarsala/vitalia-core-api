from src.utils.cli_helpers import clear_console
from src.controllers.user_controller import create_user
from src.controllers import menu
from rich import print
from questionary import select, confirm
from fastapi import FastAPI

api_server = FastAPI(
    description="API responsable de ofrecer recomendaciones personalizadas de recursos de bienestar en la plataforma Vitalia Selfcare.", 
    version="0.1.0",
    title="Vitalia Core")

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
                menu.check_preferences()
            case "3. Actualizar mi nombre de usuario":
                menu.change_user()
            case "4. Eliminar usuario":
                menu.delete_user()
            case "🚪 Salir":
                answer_is_yes = confirm("¿Estás seguro/a de que quieres salir?").ask()

                if answer_is_yes:
                    print("¡Nos vemos pronto 👋!")
                    break
                else:
                    continue 


 