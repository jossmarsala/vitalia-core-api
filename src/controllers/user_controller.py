# Lógica de creación de usuario y formulario

from questionary import text, password, select, checkbox
from rich import print 
# from rich.progress import track
from src.utils.cli_helpers import clear_console
from src.data import db

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

    name = text("¿Cómo te llamas?").ask()

    print("[bold]Responde las siguientes preguntas para recibir tus recomendaciones personalizadas ✨")

    disability = select(
        "¿Tienes algún tipo de discapacidad que te impida realizar actividad física?",
        choices=[
            "Sí"
            "No"
        ]
    )

    physical_activity = select(
        "¿Cuál es tu nivel de actividad física actual?",
        choices=[
            "Sedentario (muy poco o nada de ejercicio)",
            "En transición (busco mejorar mi condición física y aumentar mi nivel de actividad)",
            "Moderado (ejercicio ocasional)",
            "Activo (ejercicio regular)"
        ]
    )

    diet = select(
        "¿Cómo describirías tu dieta?",
        choices=[
            "Omnívora",
            "Vegetariana o vegana"
        ]
    )

    restrictions = checkbox(
        "¿Tienes alguna restricción alimentaria (intolerancias, alergias)?",
        choices=[
            "Ninguna restricción",
            "Intolerancia a la lactosa",
            "Celiaquía (intolerancia al gluten)",
            "Otros"
        ]
    )

    wellbeing_goals = checkbox(
        "¿Cuáles son tus metas en cuanto a tu bienestar?",
        choices=[
            "Reducir el estrés",
            "Mejorar el sueño",
            "Mejorar mi calidad de vida",
            "Conectar más con mi lado espiritual"
        ]
    )

    obstacles = checkbox(
        "¿Qué obstáculos enfrentas para mantener una rutina de bienestar?",
        choices=[
            "Falta de tiempo",
            "Cansancio o fatiga",
            "Niveles altos de autoexigencia",
            "Problemas físicos (movilidad reducida)",
            "Las limitaciones propias de mi edad no me permiten hacer todo lo que quisiera"
        ]
    )

    sleep_quality = select(
        "¿Cómo es tu calidad del sueño?",
        choices=[
            "Duermo entre 5 y 7 horas por noche",
            "Duermo más de 7 horas por noche",
            "Duermo menos de 5 horas por noche"
        ]
    )

    stress_level = select(
        "¿Sientes estrés y/o ansiedad de forma frecuente?",
        choices=[
            "Sí",
            "No"
        ]
    )

    daily_routine = select(
        "¿Cómo describirías tu rutina diaria?",
        choices=[
            "Tengo mucho tiempo libre y puedo organizar mi día con flexibilidad",
            "Tengo tiempo libre moderado",
            "Soy una persona ocupada con un horario ajustado"
        ]
    )

    lifestyle = select(
        "¿Cómo definirías tu estilo de vida?",
        choices=[
            "Soy una persona espiritual",
            "Soy entusiasta del fitness y la vida saludable",
            "Soy una persona centrada en el equilibrio personal",
            "Soy una persona enfocada en llevar un estilo de vida ecológico",
            "Soy una persona con una vida laboral intensa"
        ]
    )

    user = {
        "username": username,
        "password": password,
        "data": {
            "name": name,
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