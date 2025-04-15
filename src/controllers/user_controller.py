# Lógica de creación de usuario y formulario

from questionary import text, select, checkbox, password
from rich import print 
# from rich.progress import track
from src.utils.cli_helpers import clear_console
from src.data import db
from src.controllers.menu_controller import check_preferences
import time

def create_user() -> list :
    print("[bold]¡Comencemos a crear tu usuario 🌷!")

    while True:
        username = text("Crea un nombre de usuario").ask()

        if username and username.isalnum():
            break

        print("[bold red]Tu nombre de usuario solo puede estar compuesto por letras y números, intentalo de nuevo.")
        continue

    while True:
        pwd = password("Crea una contraseña").ask()

        if pwd and len(pwd) > 7:
            break
        
        print("[bold red]Tu contraseña debe tener más de 8 caracteres, intentalo de nuevo.")
        continue

    while True:
        confirm_password = password("Confirma la contraseña").ask()
        
        if confirm_password == pwd:
            break
        
        print("[bold red]Las contraseñas no coinciden.")
        continue

    name = text("¿Cómo te llamas?").ask()

    print("[bold]Responde las siguientes preguntas para recibir tus recomendaciones personalizadas ✨")

    disability = select(
        "¿Tienes algún tipo de discapacidad que te impida realizar actividad física?",
        choices=[
            "Sí",
            "No"
        ]
    ).ask()

    physical_activity = select(
        "¿Cuál es tu nivel de actividad física actual?",
        choices=[
            "Sedentario (muy poco o nada de ejercicio)",
            "En transición (busco mejorar mi condición física y aumentar mi nivel de actividad)",
            "Moderado (ejercicio ocasional)",
            "Activo (ejercicio regular)"
        ]
    ).ask()

    diet = select(
        "¿Cómo describirías tu dieta?",
        choices=[
            "Omnívora",
            "Vegetariana o vegana"
        ]
    ).ask()

    while True:
        restrictions = checkbox(
            "¿Tienes alguna restricción alimentaria (intolerancias, alergias)?",
            choices=[
                "Ninguna restricción",
                "Intolerancia a la lactosa",
                "Celiaquía (intolerancia al gluten)",
                "Otros"
            ]
        ).ask()

        if not restrictions:
            print("[bold red]Debes seleccionar al menos una opción.")
            continue

        break

    while True:
        wellbeing_goals = checkbox(
            "¿Cuáles son tus metas en cuanto a tu bienestar?",
            choices=[
                "Reducir el estrés",
                "Mejorar el sueño",
                "Mejorar mi calidad de vida",
                "Conectar más con mi lado espiritual"
            ]
        ).ask()

        if not wellbeing_goals:
            print("[bold red]Debes seleccionar al menos una opción.")
            continue

        break

    while True: 
        obstacles = checkbox(
            "¿Qué obstáculos enfrentas para mantener una rutina de bienestar?",
            choices=[
                "Falta de tiempo",
                "Cansancio o fatiga",
                "Niveles altos de autoexigencia",
                "Problemas físicos (movilidad reducida)",
                "Las limitaciones propias de mi edad no me permiten hacer todo lo que quisiera"
            ]
        ).ask()
        if not obstacles:
            print("[bold red]Debes seleccionar al menos una opción.")
            continue

        break       

    sleep_quality = select(
        "¿Cómo es tu calidad del sueño?",
        choices=[
            "Duermo entre 5 y 7 horas por noche",
            "Duermo más de 7 horas por noche",
            "Duermo menos de 5 horas por noche"
        ]
    ).ask()

    stress_level = select(
        "¿Sientes estrés y/o ansiedad de forma frecuente?",
        choices=[
            "Sí",
            "No"
        ]
    ).ask()

    daily_routine = select(
        "¿Cómo describirías tu rutina diaria?",
        choices=[
            "Tengo mucho tiempo libre y puedo organizar mi día con flexibilidad",
            "Tengo tiempo libre moderado",
            "Soy una persona ocupada con un horario ajustado"
        ]
    ).ask()

    lifestyle = select(
        "¿Cómo definirías tu estilo de vida?",
        choices=[
            "Soy una persona espiritual",
            "Soy entusiasta del fitness y la vida saludable",
            "Soy una persona centrada en el equilibrio personal",
            "Soy una persona enfocada en llevar un estilo de vida ecológico",
            "Soy una persona con una vida laboral intensa"
        ]
    ).ask()

    user = {
        "username": username.lower(),
        "password": pwd,
        "data": {
            "name": name.title(),
            "daily_routine": daily_routine,
            "diet": diet,
            "disability": disability,
            "Lifestyle": lifestyle,
            "obstacles": obstacles,
            "physical_activity": physical_activity,
            "restrictions": restrictions,
            "sleep_quality": sleep_quality,
            "stress_level": stress_level,
            "wellbeing_goals": wellbeing_goals
        }
    }

    # Guardar el usuario en la base de datos

    print(f"[bold] ¡Hola, {user["data"]["name"]}! Ya puedes ver tus recomendaciones.")
    time.sleep(5)

    # match()
    # check_preferences()