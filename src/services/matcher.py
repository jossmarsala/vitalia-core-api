# Lógica de creación de usuario y formulario

from questionary import text, password
from rich import print
from rich.progress import track
from src.utils.cli_helpers import clear_console

def create_user() -> list :
    print("[bold]¡Comencemos a crear tu usuario 🌷!")

    username = text("Crea un nombre de usuario").ask()
        
    while username.isalnum() == False:
        clear_console()
        print("Tu nombre de usuario solo puede estar compuesto por letras y números, intentalo de nuevo.")
        username = text("Crea un nombre de usuario").ask()

    password = password("Crea una contraseña").ask()

    confirm_password = password("Confirma la contraseña").ask()

    while confirm_password != password:
        clear_console()
        print("Las contraseñas no coinciden.")
        confirm_password = password("Confirma la contraseña").ask()

    name = username = text("¿Cómo te llamas?").ask()

    print("[bold]Responde las siguientes preguntas para recibir recomendaciones personalizadas ✨")

    disability = select(
        "¿Tienes algún tipo de discapacidad que te impida realizar actividad física?",
        choices=[
            "Sí"
            "No"
        ]
    )

    disability = select(
        "¿Cuál es tu nivel de actividad física actual?",
        choices=[
            "Sedentario (muy poco o nada de ejercicio)",
            "En transición (busco mejorar mi condición física y aumentar mi nivel de actividad)",
            "Moderado (ejercicio ocasional)",
            "Activo (ejercicio regular)"
        ]
    )






