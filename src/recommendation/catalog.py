"""
Static resource catalog — 36 Vitalia resources.

Each resource is defined with:
  - id: Canonical slug matching the frontend JSON data files
  - category: "diet", "routine", or "article"
  - features: Set of feature tags this resource is relevant to
  - weights: Per-feature scoring weight (how strongly each feature matters)
  - penalty_if_missing: Features that MUST be present to avoid a penalty
    (e.g. disability routines should not appear for non-disabled users)

Weight scale:
  4.0 — Hard requirement (resource is specifically designed for this feature)
  3.0 — Primary relevance (resource's main purpose aligns with this feature)
  2.0 — Strong secondary relevance
  1.5 — Supporting relevance
  1.0 — Mild relevance (default)

Penalty: -10.0 applied when a penalty_if_missing feature is absent from user profile.
"""

from dataclasses import dataclass, field
from typing import Dict, FrozenSet

from .features import *


@dataclass(frozen=True)
class Resource:
    id: str
    category: str  # "diet" | "routine" | "article"
    features: FrozenSet[str]
    weights: Dict[str, float]
    penalty_if_missing: FrozenSet[str] = field(default_factory=frozenset)


# ──────────────────────────────────────────────────────────────────────
# DIETS (12)
# ──────────────────────────────────────────────────────────────────────

DIET_01 = Resource(
    id="aliviar-la-ansiedad-en-dias-estresantes",
    category="diet",
    features=frozenset({
        STRESS_YES, GOAL_REDUCE_STRESS, SLEEP_PROBLEMS,
    }),
    weights={
        STRESS_YES: 3.0,
        GOAL_REDUCE_STRESS: 3.0,
        SLEEP_PROBLEMS: 1.5,
    },
)

DIET_02 = Resource(
    id="dias-ocupados",
    category="diet",
    features=frozenset({
        ROUTINE_BUSY, OBSTACLE_TIME, LIFESTYLE_WORK_INTENSIVE,
    }),
    weights={
        ROUTINE_BUSY: 3.0,
        OBSTACLE_TIME: 3.0,
        LIFESTYLE_WORK_INTENSIVE: 2.0,
    },
)

DIET_03 = Resource(
    id="energia-y-vitalidad",
    category="diet",
    features=frozenset({
        GOAL_IMPROVE_QUALITY, ACTIVITY_MODERATE, ACTIVITY_ACTIVE,
        DIET_OMNIVORE, RESTRICTION_NONE,
    }),
    weights={
        GOAL_IMPROVE_QUALITY: 2.0,
        ACTIVITY_MODERATE: 2.0,
        ACTIVITY_ACTIVE: 2.0,
        DIET_OMNIVORE: 1.5,
        RESTRICTION_NONE: 1.0,
    },
)

DIET_04 = Resource(
    id="express-vegetariana",
    category="diet",
    features=frozenset({
        DIET_VEGETARIAN, ROUTINE_BUSY, OBSTACLE_TIME,
    }),
    weights={
        DIET_VEGETARIAN: 4.0,
        ROUTINE_BUSY: 2.0,
        OBSTACLE_TIME: 2.0,
    },
    penalty_if_missing=frozenset({DIET_VEGETARIAN}),
)

DIET_05 = Resource(
    id="fin-de-semana-sin-lacteos",
    category="diet",
    features=frozenset({
        RESTRICTION_LACTOSE, ROUTINE_MODERATE_FREE,
    }),
    weights={
        RESTRICTION_LACTOSE: 4.0,
        ROUTINE_MODERATE_FREE: 1.5,
    },
    penalty_if_missing=frozenset({RESTRICTION_LACTOSE}),
)

DIET_06 = Resource(
    id="sin-lacteos",
    category="diet",
    features=frozenset({
        RESTRICTION_LACTOSE,
    }),
    weights={
        RESTRICTION_LACTOSE: 4.0,
    },
    penalty_if_missing=frozenset({RESTRICTION_LACTOSE}),
)

DIET_07 = Resource(
    id="sueno-reparador",
    category="diet",
    features=frozenset({
        GOAL_IMPROVE_SLEEP, SLEEP_PROBLEMS, STRESS_YES,
    }),
    weights={
        GOAL_IMPROVE_SLEEP: 3.0,
        SLEEP_PROBLEMS: 3.0,
        STRESS_YES: 1.5,
    },
)

DIET_08 = Resource(
    id="plan-de-comidas-con-minima-preparacion-y-cero-esfuerzo-fisico",
    category="diet",
    features=frozenset({
        DISABILITY_YES, OBSTACLE_PHYSICAL, ACTIVITY_SEDENTARY,
        OBSTACLE_ELDERLY,
    }),
    weights={
        DISABILITY_YES: 4.0,
        OBSTACLE_PHYSICAL: 3.0,
        ACTIVITY_SEDENTARY: 2.0,
        OBSTACLE_ELDERLY: 2.0,
    },
)

DIET_09 = Resource(
    id="plan-entrenamiento-recuperacion",
    category="diet",
    features=frozenset({
        ACTIVITY_ACTIVE, LIFESTYLE_FITNESS, GOAL_IMPROVE_QUALITY,
        DIET_OMNIVORE,
    }),
    weights={
        ACTIVITY_ACTIVE: 3.0,
        LIFESTYLE_FITNESS: 3.0,
        GOAL_IMPROVE_QUALITY: 1.5,
        DIET_OMNIVORE: 1.0,
    },
)

DIET_10 = Resource(
    id="plan-semanas-ocupadas",
    category="diet",
    features=frozenset({
        ROUTINE_BUSY, OBSTACLE_TIME, SLEEP_5TO7H,
        LIFESTYLE_WORK_INTENSIVE,
    }),
    weights={
        ROUTINE_BUSY: 3.0,
        OBSTACLE_TIME: 2.0,
        SLEEP_5TO7H: 1.5,
        LIFESTYLE_WORK_INTENSIVE: 2.0,
    },
)

DIET_11 = Resource(
    id="plan-alto-foco-mental",
    category="diet",
    features=frozenset({
        GOAL_IMPROVE_QUALITY, LIFESTYLE_WORK_INTENSIVE, STRESS_YES,
        OBSTACLE_SELF_DEMAND,
    }),
    weights={
        GOAL_IMPROVE_QUALITY: 2.0,
        LIFESTYLE_WORK_INTENSIVE: 2.0,
        STRESS_YES: 3.0,
        OBSTACLE_SELF_DEMAND: 3.0,
    },
)

DIET_12 = Resource(
    id="plan-estabilidad-energetica",
    category="diet",
    features=frozenset({
        OBSTACLE_FATIGUE, GOAL_IMPROVE_QUALITY, ACTIVITY_TRANSITION,
    }),
    weights={
        OBSTACLE_FATIGUE: 3.0,
        GOAL_IMPROVE_QUALITY: 2.0,
        ACTIVITY_TRANSITION: 2.0,
    },
)


# ──────────────────────────────────────────────────────────────────────
# ROUTINES (10)
# ──────────────────────────────────────────────────────────────────────

ROUTINE_01 = Resource(
    id="cuerpo-completo-en-casa",
    category="routine",
    features=frozenset({
        ACTIVITY_TRANSITION, ACTIVITY_MODERATE, DISABILITY_NO,
        OBSTACLE_TIME,
    }),
    weights={
        ACTIVITY_TRANSITION: 2.0,
        ACTIVITY_MODERATE: 2.0,
        DISABILITY_NO: 1.0,
        OBSTACLE_TIME: 1.5,
    },
    penalty_if_missing=frozenset({DISABILITY_NO}),
)

ROUTINE_02 = Resource(
    id="entrenamiento-en-15-minutos",
    category="routine",
    features=frozenset({
        ACTIVITY_MODERATE, OBSTACLE_TIME, ROUTINE_BUSY,
    }),
    weights={
        ACTIVITY_MODERATE: 2.0,
        OBSTACLE_TIME: 3.0,
        ROUTINE_BUSY: 3.0,
    },
)

ROUTINE_03 = Resource(
    id="fuerza-silla-de-ruedas",
    category="routine",
    features=frozenset({
        DISABILITY_YES, OBSTACLE_PHYSICAL, ACTIVITY_SEDENTARY,
        ACTIVITY_TRANSITION,
    }),
    weights={
        DISABILITY_YES: 4.0,
        OBSTACLE_PHYSICAL: 3.0,
        ACTIVITY_SEDENTARY: 1.5,
        ACTIVITY_TRANSITION: 1.5,
    },
    penalty_if_missing=frozenset({DISABILITY_YES}),
)

ROUTINE_04 = Resource(
    id="abdomen-y-estabilidad-core",
    category="routine",
    features=frozenset({
        ACTIVITY_TRANSITION, ACTIVITY_MODERATE, DISABILITY_NO,
        GOAL_IMPROVE_QUALITY,
    }),
    weights={
        ACTIVITY_TRANSITION: 2.0,
        ACTIVITY_MODERATE: 2.0,
        DISABILITY_NO: 1.0,
        GOAL_IMPROVE_QUALITY: 1.5,
    },
    penalty_if_missing=frozenset({DISABILITY_NO}),
)

ROUTINE_05 = Resource(
    id="yoga-suave-relajacion",
    category="routine",
    features=frozenset({
        GOAL_REDUCE_STRESS, STRESS_YES, LIFESTYLE_SPIRITUAL,
        LIFESTYLE_BALANCE, SLEEP_PROBLEMS,
    }),
    weights={
        GOAL_REDUCE_STRESS: 3.0,
        STRESS_YES: 3.0,
        LIFESTYLE_SPIRITUAL: 2.0,
        LIFESTYLE_BALANCE: 1.5,
        SLEEP_PROBLEMS: 1.5,
    },
)

ROUTINE_06 = Resource(
    id="calistenia-outdoor-fuerza",
    category="routine",
    features=frozenset({
        ACTIVITY_ACTIVE, LIFESTYLE_FITNESS, DISABILITY_NO,
    }),
    weights={
        ACTIVITY_ACTIVE: 3.0,
        LIFESTYLE_FITNESS: 3.0,
        DISABILITY_NO: 1.0,
    },
    penalty_if_missing=frozenset({DISABILITY_NO}),
)

ROUTINE_07 = Resource(
    id="movilidad-fuerza-suave-adultos-mayores",
    category="routine",
    features=frozenset({
        OBSTACLE_ELDERLY, ACTIVITY_SEDENTARY, ACTIVITY_TRANSITION,
        DISABILITY_YES,
    }),
    weights={
        OBSTACLE_ELDERLY: 4.0,
        ACTIVITY_SEDENTARY: 2.0,
        ACTIVITY_TRANSITION: 2.0,
        DISABILITY_YES: 1.5,
    },
)

ROUTINE_08 = Resource(
    id="fuerza-inferior-gluteos-casa",
    category="routine",
    features=frozenset({
        ACTIVITY_MODERATE, ACTIVITY_ACTIVE, LIFESTYLE_FITNESS,
        DISABILITY_NO, GOAL_IMPROVE_QUALITY,
    }),
    weights={
        ACTIVITY_MODERATE: 2.0,
        ACTIVITY_ACTIVE: 2.0,
        LIFESTYLE_FITNESS: 3.0,
        DISABILITY_NO: 1.0,
        GOAL_IMPROVE_QUALITY: 1.0,
    },
    penalty_if_missing=frozenset({DISABILITY_NO}),
)

ROUTINE_09 = Resource(
    id="traccion-fuerza-espalda-postura",
    category="routine",
    features=frozenset({
        OBSTACLE_FATIGUE, LIFESTYLE_WORK_INTENSIVE,
        ACTIVITY_TRANSITION, ACTIVITY_MODERATE,
    }),
    weights={
        OBSTACLE_FATIGUE: 2.0,
        LIFESTYLE_WORK_INTENSIVE: 3.0,
        ACTIVITY_TRANSITION: 2.0,
        ACTIVITY_MODERATE: 1.5,
    },
)

ROUTINE_10 = Resource(
    id="movilidad-suave-antes-de-dormir",
    category="routine",
    features=frozenset({
        GOAL_IMPROVE_SLEEP, SLEEP_PROBLEMS, STRESS_YES,
    }),
    weights={
        GOAL_IMPROVE_SLEEP: 3.0,
        SLEEP_PROBLEMS: 3.0,
        STRESS_YES: 2.0,
    },
)


# ──────────────────────────────────────────────────────────────────────
# ARTICLES (14)
# ──────────────────────────────────────────────────────────────────────

ARTICLE_01 = Resource(
    id="pausas-activas",
    category="article",
    features=frozenset({
        LIFESTYLE_WORK_INTENSIVE, OBSTACLE_TIME, ROUTINE_BUSY,
    }),
    weights={
        LIFESTYLE_WORK_INTENSIVE: 3.0,
        OBSTACLE_TIME: 2.0,
        ROUTINE_BUSY: 2.0,
    },
)

ARTICLE_02 = Resource(
    id="enfoque-integral-trabajo",
    category="article",
    features=frozenset({
        LIFESTYLE_WORK_INTENSIVE, GOAL_IMPROVE_QUALITY, OBSTACLE_SELF_DEMAND,
    }),
    weights={
        LIFESTYLE_WORK_INTENSIVE: 3.0,
        GOAL_IMPROVE_QUALITY: 1.5,
        OBSTACLE_SELF_DEMAND: 2.0,
    },
)

ARTICLE_03 = Resource(
    id="autocuidado-habitos",
    category="article",
    features=frozenset({
        GOAL_IMPROVE_QUALITY, OBSTACLE_FATIGUE,
    }),
    weights={
        GOAL_IMPROVE_QUALITY: 2.0,
        OBSTACLE_FATIGUE: 2.0,
    },
)

ARTICLE_04 = Resource(
    id="siestas-cortas",
    category="article",
    features=frozenset({
        SLEEP_5TO7H, SLEEP_PROBLEMS, OBSTACLE_FATIGUE, ROUTINE_MODERATE_FREE,
    }),
    weights={
        SLEEP_5TO7H: 2.0,
        SLEEP_PROBLEMS: 2.0,
        OBSTACLE_FATIGUE: 2.0,
        ROUTINE_MODERATE_FREE: 1.5,
    },
)

ARTICLE_05 = Resource(
    id="tecnicas-estres",
    category="article",
    features=frozenset({
        STRESS_YES, GOAL_REDUCE_STRESS, OBSTACLE_SELF_DEMAND,
    }),
    weights={
        STRESS_YES: 3.0,
        GOAL_REDUCE_STRESS: 3.0,
        OBSTACLE_SELF_DEMAND: 2.0,
    },
)

ARTICLE_06 = Resource(
    id="alimentacion-consciente",
    category="article",
    features=frozenset({
        GOAL_IMPROVE_QUALITY, LIFESTYLE_BALANCE, LIFESTYLE_ECOLOGICAL,
    }),
    weights={
        GOAL_IMPROVE_QUALITY: 2.0,
        LIFESTYLE_BALANCE: 2.0,
        LIFESTYLE_ECOLOGICAL: 2.0,
    },
)

ARTICLE_07 = Resource(
    id="actividad-fisica-facil",
    category="article",
    features=frozenset({
        DISABILITY_YES, OBSTACLE_PHYSICAL, ACTIVITY_SEDENTARY,
    }),
    weights={
        DISABILITY_YES: 4.0,
        OBSTACLE_PHYSICAL: 3.0,
        ACTIVITY_SEDENTARY: 2.0,
    },
)

ARTICLE_08 = Resource(
    id="vida-sostenible",
    category="article",
    features=frozenset({
        LIFESTYLE_ECOLOGICAL, GOAL_IMPROVE_QUALITY,
    }),
    weights={
        LIFESTYLE_ECOLOGICAL: 3.0,
        GOAL_IMPROVE_QUALITY: 1.5,
    },
)

ARTICLE_09 = Resource(
    id="dieta-plantas",
    category="article",
    features=frozenset({
        DIET_VEGETARIAN, LIFESTYLE_ECOLOGICAL, LIFESTYLE_BALANCE,
    }),
    weights={
        DIET_VEGETARIAN: 3.0,
        LIFESTYLE_ECOLOGICAL: 2.0,
        LIFESTYLE_BALANCE: 1.5,
    },
)

ARTICLE_10 = Resource(
    id="rutina-nocturna",
    category="article",
    features=frozenset({
        GOAL_IMPROVE_SLEEP, SLEEP_PROBLEMS, STRESS_YES,
    }),
    weights={
        GOAL_IMPROVE_SLEEP: 3.0,
        SLEEP_PROBLEMS: 3.0,
        STRESS_YES: 1.5,
    },
)

ARTICLE_11 = Resource(
    id="tecnica-15-minutos",
    category="article",
    features=frozenset({
        LIFESTYLE_WORK_INTENSIVE, OBSTACLE_TIME, GOAL_IMPROVE_QUALITY,
    }),
    weights={
        LIFESTYLE_WORK_INTENSIVE: 2.0,
        OBSTACLE_TIME: 3.0,
        GOAL_IMPROVE_QUALITY: 1.5,
    },
)

ARTICLE_12 = Resource(
    id="mente-activa",
    category="article",
    features=frozenset({
        OBSTACLE_ELDERLY, GOAL_IMPROVE_QUALITY, LIFESTYLE_BALANCE,
    }),
    weights={
        OBSTACLE_ELDERLY: 4.0,
        GOAL_IMPROVE_QUALITY: 2.0,
        LIFESTYLE_BALANCE: 1.5,
    },
)

ARTICLE_13 = Resource(
    id="nutricion-discapacidad",
    category="article",
    features=frozenset({
        DISABILITY_YES, OBSTACLE_PHYSICAL,
    }),
    weights={
        DISABILITY_YES: 4.0,
        OBSTACLE_PHYSICAL: 3.0,
    },
    penalty_if_missing=frozenset({DISABILITY_YES}),
)

ARTICLE_14 = Resource(
    id="relajacion-movilidad",
    category="article",
    features=frozenset({
        DISABILITY_YES, GOAL_REDUCE_STRESS, STRESS_YES,
        OBSTACLE_PHYSICAL,
    }),
    weights={
        DISABILITY_YES: 4.0,
        GOAL_REDUCE_STRESS: 2.0,
        STRESS_YES: 2.0,
        OBSTACLE_PHYSICAL: 2.0,
    },
    penalty_if_missing=frozenset({DISABILITY_YES}),
)


# ──────────────────────────────────────────────────────────────────────
# Catalog aggregation
# ──────────────────────────────────────────────────────────────────────

ALL_RESOURCES: list[Resource] = [
    # Diets
    DIET_01, DIET_02, DIET_03, DIET_04, DIET_05, DIET_06,
    DIET_07, DIET_08, DIET_09, DIET_10, DIET_11, DIET_12,
    # Routines
    ROUTINE_01, ROUTINE_02, ROUTINE_03, ROUTINE_04, ROUTINE_05,
    ROUTINE_06, ROUTINE_07, ROUTINE_08, ROUTINE_09, ROUTINE_10,
    # Articles
    ARTICLE_01, ARTICLE_02, ARTICLE_03, ARTICLE_04, ARTICLE_05,
    ARTICLE_06, ARTICLE_07, ARTICLE_08, ARTICLE_09, ARTICLE_10,
    ARTICLE_11, ARTICLE_12, ARTICLE_13, ARTICLE_14,
]

# Pre-indexed by category for fast lookup
DIETS = [r for r in ALL_RESOURCES if r.category == "diet"]
ROUTINES = [r for r in ALL_RESOURCES if r.category == "routine"]
ARTICLES = [r for r in ALL_RESOURCES if r.category == "article"]

# Sanity checks at import time
assert len(DIETS) == 12, f"Expected 12 diets, got {len(DIETS)}"
assert len(ROUTINES) == 10, f"Expected 10 routines, got {len(ROUTINES)}"
assert len(ARTICLES) == 14, f"Expected 14 articles, got {len(ARTICLES)}"
assert len(ALL_RESOURCES) == 36, f"Expected 36 resources, got {len(ALL_RESOURCES)}"
