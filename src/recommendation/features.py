"""
Feature vocabulary and user feature extraction.

Defines the canonical set of feature tags used to describe both resources
and user profiles. Each feature is a namespaced string "dimension:value".

The extract_user_features() function converts raw questionnaire answers
(as sent by the frontend) into a set of feature tags for scoring.
"""

import logging
from typing import Set

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────
# Feature constants — organized by questionnaire dimension
# ──────────────────────────────────────────────────────────────────────

# Disability
DISABILITY_YES = "disability:yes"
DISABILITY_NO = "disability:no"

# Physical activity level
ACTIVITY_SEDENTARY = "activity:sedentary"
ACTIVITY_TRANSITION = "activity:transition"
ACTIVITY_MODERATE = "activity:moderate"
ACTIVITY_ACTIVE = "activity:active"

# Diet type
DIET_OMNIVORE = "diet:omnivore"
DIET_VEGETARIAN = "diet:vegetarian"

# Dietary restrictions
RESTRICTION_NONE = "restriction:none"
RESTRICTION_LACTOSE = "restriction:lactose"
RESTRICTION_GLUTEN = "restriction:gluten"

# Wellbeing goals
GOAL_REDUCE_STRESS = "goal:reduce_stress"
GOAL_IMPROVE_SLEEP = "goal:improve_sleep"
GOAL_IMPROVE_QUALITY = "goal:improve_quality"
GOAL_SPIRITUAL = "goal:spiritual"

# Obstacles
OBSTACLE_TIME = "obstacle:time"
OBSTACLE_FATIGUE = "obstacle:fatigue"
OBSTACLE_SELF_DEMAND = "obstacle:self_demand"
OBSTACLE_PHYSICAL = "obstacle:physical"
OBSTACLE_ELDERLY = "obstacle:elderly"

# Sleep quality
SLEEP_5TO7H = "sleep:5to7h"
SLEEP_GOOD = "sleep:good"
SLEEP_PROBLEMS = "sleep:problems"

# Stress level
STRESS_YES = "stress:yes"
STRESS_NO = "stress:no"

# Daily routine
ROUTINE_FREE = "routine:free"
ROUTINE_MODERATE_FREE = "routine:moderate_free"
ROUTINE_BUSY = "routine:busy"

# Lifestyle
LIFESTYLE_SPIRITUAL = "lifestyle:spiritual"
LIFESTYLE_FITNESS = "lifestyle:fitness"
LIFESTYLE_BALANCE = "lifestyle:balance"
LIFESTYLE_ECOLOGICAL = "lifestyle:ecological"
LIFESTYLE_WORK_INTENSIVE = "lifestyle:work_intensive"


# ──────────────────────────────────────────────────────────────────────
# Value mappings — exact strings from form.html → feature tags
#
# Each map uses .lower().strip() normalization for resilience.
# The keys are the exact `value="..."` attributes from the HTML form,
# lowercased. Accented characters are preserved (they match after .lower()).
# ──────────────────────────────────────────────────────────────────────

_DISABILITY_MAP = {
    "sí": DISABILITY_YES,
    "si": DISABILITY_YES,       # accent-less variant
    "no": DISABILITY_NO,
}

_PHYSICAL_ACTIVITY_MAP = {
    "sedentario": ACTIVITY_SEDENTARY,
    "en transición": ACTIVITY_TRANSITION,
    "en transicion": ACTIVITY_TRANSITION,  # accent-less variant
    "moderado": ACTIVITY_MODERATE,
    "activo": ACTIVITY_ACTIVE,
}

_DIET_MAP = {
    "vegetariana": DIET_VEGETARIAN,
    "vegana": DIET_VEGETARIAN,         # treated same as vegetariana
    "omnívora": DIET_OMNIVORE,
    "omnivora": DIET_OMNIVORE,         # accent-less variant
}

_RESTRICTION_MAP = {
    "ninguna restricción": RESTRICTION_NONE,
    "ninguna restriccion": RESTRICTION_NONE,
    "intolerancia a la lactosa": RESTRICTION_LACTOSE,
    "celiaquía": RESTRICTION_GLUTEN,
    "celiaquia": RESTRICTION_GLUTEN,
}

_WELLBEING_GOALS_MAP = {
    "reducir el estrés": GOAL_REDUCE_STRESS,
    "reducir el estres": GOAL_REDUCE_STRESS,
    "mejorar el sueño": GOAL_IMPROVE_SLEEP,
    "mejorar el sueno": GOAL_IMPROVE_SLEEP,
    "aumentar mi calidad de vida": GOAL_IMPROVE_QUALITY,
    "conectar más con mi lado espiritual": GOAL_SPIRITUAL,
    "conectar mas con mi lado espiritual": GOAL_SPIRITUAL,
}

_OBSTACLES_MAP = {
    "falta de tiempo": OBSTACLE_TIME,
    "cansancio o fatiga": OBSTACLE_FATIGUE,
    "niveles altos de autoexigencia": OBSTACLE_SELF_DEMAND,
    "problemas físicos (movilidad reducida)": OBSTACLE_PHYSICAL,
    "problemas fisicos (movilidad reducida)": OBSTACLE_PHYSICAL,
    "soy una persona muy mayor": OBSTACLE_ELDERLY,
}

_SLEEP_QUALITY_MAP = {
    "duermo entre 5 y 7 horas por noche": SLEEP_5TO7H,
    "duermo más de 7 horas por noche": SLEEP_GOOD,
    "duermo mas de 7 horas por noche": SLEEP_GOOD,
    "tengo problemas para dormir": SLEEP_PROBLEMS,
}

_STRESS_MAP = {
    "alto": STRESS_YES,
    "bajo": STRESS_NO,
}

_DAILY_ROUTINE_MAP = {
    "tengo mucho tiempo libre y puedo organizar mi día con flexibilidad": ROUTINE_FREE,
    "tengo mucho tiempo libre y puedo organizar mi dia con flexibilidad": ROUTINE_FREE,
    "tengo tiempo libre moderado": ROUTINE_MODERATE_FREE,
    "soy una persona ocupada con un horario ajustado": ROUTINE_BUSY,
}

_LIFESTYLE_MAP = {
    "soy una persona espiritual": LIFESTYLE_SPIRITUAL,
    "soy entusiasta del fitness y la vida saludable": LIFESTYLE_FITNESS,
    "soy una persona centrada en el equilibrio personal": LIFESTYLE_BALANCE,
    "soy una persona enfocada en llevar un estilo de vida ecológico": LIFESTYLE_ECOLOGICAL,
    "soy una persona enfocada en llevar un estilo de vida ecologico": LIFESTYLE_ECOLOGICAL,
    "soy una persona con una vida laboral intensa": LIFESTYLE_WORK_INTENSIVE,
}


from typing import Optional

def _map_single(raw_value: str, mapping: dict[str, str], field_name: str) -> Optional[str]:
    """Map a single raw form value to a feature tag using the given mapping."""
    if not raw_value:
        return None
    normalized = raw_value.strip().lower()
    tag = mapping.get(normalized)
    if tag is None:
        logger.warning(f"Valor no reconocido para '{field_name}': '{raw_value}'")
    return tag


def _map_list(raw_values: list, mapping: dict[str, str], field_name: str) -> list[str]:
    """Map a list of raw form values to feature tags."""
    tags = []
    for val in raw_values:
        tag = _map_single(str(val), mapping, field_name)
        if tag is not None:
            tags.append(tag)
    return tags


def extract_user_features(user_data: dict) -> Set[str]:
    """
    Convert raw questionnaire answers into a set of feature tags.
    
    Args:
        user_data: Dict with keys matching the API schema fields
                   (disability, physicalActivity, diet, restrictions,
                    wellbeingGoals, obstacles, sleepQuality, stressLevel,
                    dailyRoutine, lifestyle).
    
    Returns:
        A set of canonical feature tag strings ready for scoring.
    """
    features: Set[str] = set()

    # Single-value fields
    single_mappings = [
        ("disability", _DISABILITY_MAP),
        ("physicalActivity", _PHYSICAL_ACTIVITY_MAP),
        ("diet", _DIET_MAP),
        ("sleepQuality", _SLEEP_QUALITY_MAP),
        ("stressLevel", _STRESS_MAP),
        ("dailyRoutine", _DAILY_ROUTINE_MAP),
        ("lifestyle", _LIFESTYLE_MAP),
    ]

    for field_name, mapping in single_mappings:
        raw = user_data.get(field_name, "")
        tag = _map_single(str(raw), mapping, field_name)
        if tag:
            features.add(tag)

    # Multi-value fields (checkboxes)
    multi_mappings = [
        ("restrictions", _RESTRICTION_MAP),
        ("wellbeingGoals", _WELLBEING_GOALS_MAP),
        ("obstacles", _OBSTACLES_MAP),
    ]

    for field_name, mapping in multi_mappings:
        raw_list = user_data.get(field_name, [])
        if isinstance(raw_list, str):
            raw_list = [raw_list]
        tags = _map_list(raw_list, mapping, field_name)
        features.update(tags)

    logger.debug(f"Extracted {len(features)} features from user data: {features}")
    return features
