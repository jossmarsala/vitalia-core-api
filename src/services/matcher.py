# Lógica de matching

from rich import print 
from rich.progress import track
from src.utils.file_helpers import read_json
from src.config.settings import RESOURCES_JSON

def match_preferences(user: dict) -> list[dict]:
    read_resources = read_json(RESOURCES_JSON)

    article_alimentacion_consciente = [0, read_resources[0]['data']]
    article_dieta_base_plantas = [0, read_resources[1]['data']]
    article_ejercicio_movilidad_reducida = [0, read_resources[2]['data']]
    article_habitos_autocuidado = [0, read_resources[3]['data']]
    article_integral_trabajo = [0, read_resources[4]['data']]
    article_manejo_estres = [0, read_resources[5]['data']]
    article_mente_activa = [0, read_resources[6]['data']]
    article_nutricion_discapacidad = [0, read_resources[7]['data']]
    article_pausas_activas = [0, read_resources[8]['data']]
    article_rutina_nocturna = [0, read_resources[9]['data']]
    article_salud_mental_discapacidad = [0, read_resources[10]['data']]
    article_siestas_cortas = [0, read_resources[11]['data']]
    article_tecnica_15_minutos = [0, read_resources[12]['data']]
    article_vida_sostenible = [0, read_resources[13]['data']]
    diet_descanso_reparador = [0, read_resources[14]['data']]
    diet_dia_ocupado = [0, read_resources[15]['data']]
    diet_dias_estresantes = [0, read_resources[16]['data']]
    diet_energia_vitalidad = [0, read_resources[17]['data']]
    diet_semanal_celiaquia = [0, read_resources[18]['data']]
    diet_semanal_sin_lacteos = [0, read_resources[19]['data']]
    diet_semanal_vegetariana = [0, read_resources[20]['data']]
    diet_weekend_sin_lacteos = [0, read_resources[21]['data']]
    routine_cardio_funcional_express = [0, read_resources[22]['data']]
    routine_circuito_funcional_adaptado = [0, read_resources[23]['data']]
    routine_cuerpo_completo_express = [0, read_resources[24]['data']]
    routine_ejercicios_mejorar_postura = [0, read_resources[25]['data']]
    routine_entrenamiento_matutino = [0, read_resources[26]['data']]
    routine_fortalecer_espalda = [0, read_resources[27]['data']]
    routine_fuerza_energia = [0, read_resources[28]['data']]
    routine_hiit_liberar_tension = [0, read_resources[29]['data']]
    routine_yoga_movilidad_reducida = [0, read_resources[30]['data']]
    routine_yoga_suave = [0, read_resources[31]['data']]

    for resource in read_resources:
        for key, value in resource["data"].items():
            if key in user["data"] and user["data"][key] == value:
                print(f"Match! {key} se encuentra en user y vale {value}")
            
