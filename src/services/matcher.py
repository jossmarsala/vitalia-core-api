# Lógica de matching

from rich import print
from questionary import confirm
from src.utils.file_helpers import read_json
from src.config.settings import RESOURCES_JSON
import time
from typing import Optional


def match_preferences(user: dict) -> list[dict]:
    read_resources = read_json(RESOURCES_JSON)

    articles = [
        {"id": "article_alimentacion_consciente", "points": 0},
        {"id": "article_dieta_base_plantas", "points": 0},
        {"id": "article_ejercicio_movilidad_reducida", "points": 0},
        {"id": "article_habitos_autocuidado", "points": 0},
        {"id": "article_integral_trabajo", "points": 0},
        {"id": "article_manejo_estres", "points": 0},
        {"id": "article_mente_activa", "points": 0},
        {"id": "article_nutricion_discapacidad", "points": 0},
        {"id": "article_pausas_activas", "points": 0},
        {"id": "article_rutina_nocturna", "points": 0},
        {"id": "article_salud_mental_discapacidad", "points": 0},
        {"id": "article_siestas_cortas", "points": 0},
        {"id": "article_tecnica_15_minutos", "points": 0},
        {"id": "article_vida_sostenible", "points": 0},
        {"id": "diet_descanso_reparador", "points": 0},
        {"id": "diet_dia_ocupado", "points": 0},
        {"id": "diet_dias_estresantes", "points": 0},
        {"id": "diet_energia_vitalidad", "points": 0},
        {"id": "diet_semanal_celiaquia", "points": 0},
        {"id": "diet_semanal_sin_lacteos", "points": 0},
        {"id": "diet_semanal_vegetariana", "points": 0},
        {"id": "diet_weekend_sin_lacteos", "points": 0},
        {"id": "routine_cardio_funcional_express", "points": 0},
        {"id": "routine_circuito_funcional_adaptado", "points": 0},
        {"id": "routine_cuerpo_completo_express", "points": 0},
        {"id": "routine_ejercicios_mejorar_postura", "points": 0},
        {"id": "routine_entrenamiento_matutino", "points": 0},
        {"id": "routine_fortalecer_espalda", "points": 0},
        {"id": "routine_fuerza_energia", "points": 0},
        {"id": "routine_hiit_liberar_tension", "points": 0},
        {"id": "routine_yoga_movilidad_reducida", "points": 0},
        {"id": "routine_yoga_suave", "points": 0}
    ]

    for resource in read_resources:
        for key, value in resource["data"].items():
            if key in user["data"] and user["data"][key] == value:
                for article in articles:
                    if resource["id"] == article["id"]:
                        article["points"] += 1
            elif type(user["data"][key]) is list:
                if key in user["data"] and value in user["data"][key]:
                    for article in articles:
                        if resource["id"] == article["id"]:
                            article["points"] += 1

    print("\n¡Listo! Ahora te mostraremos recursos que podrían ayudarte a alcanzar tus metas de bienestar:\n")

    def __show_first_four(kind: str, min_points : Optional[int] = 1 ):
        filtered = [a for a in articles if a["id"].startswith(kind) and a["points"] >= min_points]
        first_four = sorted(filtered, key=lambda x: x["points"], reverse=True)[:4]

        for article in first_four:
            for resource in read_resources:
                if resource["id"] == article["id"]:
                    print(f"   - {resource['title']}")

    print("[bold]Lecturas y artículos:")
    __show_first_four("article")
    print("\n[bold]Rutinas de ejercicio:")
    __show_first_four("routine")
    print("\n[bold]Planes alimenticios:")
    __show_first_four("diet")

    while True:
        answer_is_yes = confirm("¿Volver al menú principal?").ask()
        if answer_is_yes:
            break
        else:
            continue 

