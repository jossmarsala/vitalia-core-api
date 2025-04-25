from .user import UserModel
from typing import Optional
import random


class TempUserModel(UserModel):
    def __init__(self, username: str = "test_user", password: str = "12345678", data: dict = {}, auto_fill: Optional[bool] = True):
        if auto_fill:
            data = self._auto_fill_form()
        else:
            data = {}
        super().__init__(username, password, data)
        self.auto_fill = auto_fill

    def _auto_fill_form(self) -> dict:
        data = {
            "name": "Test User",
            "daily_routine": random.choice(["Tengo mucho tiempo libre y puedo organizar mi día con flexibilidad", "Tengo tiempo libre moderado", "Soy una persona ocupada con un horario ajustado"]),
            "diet": random.choice(["Omnívora", "Vegetariana o vegana"]),
            "disability": random.choice(["Sí", "No"]),
            "lifestyle": random.choice(["Soy una persona espiritual", "Soy entusiasta del fitness y la vida saludable", "Soy una persona centrada en el equilibrio personal", "Soy una persona enfocada en llevar un estilo de vida ecológico", "Soy una persona con una vida laboral intensa"]),
            "obstacles": random.choice(["Falta de tiempo", "Cansancio o fatiga", "Niveles altos de autoexigencia", "Problemas físicos (movilidad reducida)", "Las limitaciones propias de mi edad no me permiten hacer todo lo que quisiera"], 2),
            "physical_activity": random.choice(["Sedentario (muy poco o nada de ejercicio)", "En transición (busco mejorar mi condición física y aumentar mi nivel de actividad)", "Moderado (ejercicio ocasional)", "Activo (ejercicio regular)"]),
            "restrictions": random.choice(["Ninguna restricción", "Intolerancia a la lactosa", "Celiaquía (intolerancia al gluten)", "Otros"], 2),
            "sleep_quality": random.choice(["Duermo entre 5 y 7 horas por noche", "Duermo más de 7 horas por noche", "Duermo menos de 5 horas por noche"]),
            "stress_level": random.choice(["Sí", "No"]),
            "wellbeing_goals": random.choice(["Reducir el estrés", "Mejorar el sueño", "Mejorar mi calidad de vida", "Conectar más con mi lado espiritual"], 2)
        }