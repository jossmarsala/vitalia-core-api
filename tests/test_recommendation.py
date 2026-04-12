

from src.recommendation.features import extract_user_features, DISABILITY_YES, ACTIVITY_SEDENTARY
from src.recommendation.catalog import DIETS, ROUTINES, ARTICLES, Resource
from src.recommendation.scoring import score_resource, score_all, MISSING_PENALTY
from src.recommendation.engine import recommend, RecommendationResult

def test_extract_user_features():
    user_data = {
        "disability": "Sí",
        "physicalActivity": "Sedentario",
        "diet": "Omnívora",
        "restrictions": ["Intolerancia a la lactosa"],
        "wellbeingGoals": ["Mejorar calidad de vida"],
        "obstacles": ["Falta de tiempo", "Problemas físicos (movilidad reducida)"],
        "sleepQuality": "Duermo menos de 5 horas por noche",
        "stressLevel": "Alto",
        "dailyRoutine": "Soy una persona ocupada con un horario ajustado",
        "lifestyle": "Soy una persona con una vida laboral intensa"
    }
    
    features = extract_user_features(user_data)
    
    assert "disability:yes" in features
    assert "activity:sedentary" in features
    assert "diet:omnivore" in features
    assert "restriction:lactose" in features
    assert "obstacle:time" in features
    assert "obstacle:physical" in features

def test_score_resource():
    user_features = {"disability:yes", "obstacle:physical", "activity:sedentary"}
    
    # Matching routine
    routine_silla = next(r for r in ROUTINES if r.id == "fuerza-silla-de-ruedas")
    score = score_resource(user_features, routine_silla)
    assert score == 8.5 # 4.0 + 3.0 + 1.5
    
    # Non-matching routine with missing penalty
    routine_cuerpo = next(r for r in ROUTINES if r.id == "cuerpo-completo-en-casa")
    score_cuerpo = score_resource(user_features, routine_cuerpo)
    assert score_cuerpo < 0

def test_score_all():
    user_features = {"disability:yes", "obstacle:physical", "activity:sedentary"}
    scored_routines = score_all(user_features, ROUTINES)
    assert scored_routines[0][0].id == "fuerza-silla-de-ruedas"

def test_recommend_engine():
    user_data = {
        "disability": "Sí",
        "physicalActivity": "Sedentario",
        "diet": "Omnívora",
        "restrictions": [],
        "wellbeingGoals": [],
        "obstacles": ["Problemas físicos (movilidad reducida)"],
        "sleepQuality": "Duermo más de 7 horas por noche",
        "stressLevel": "Bajo",
        "dailyRoutine": "Tengo mucho tiempo libre y puedo organizar mi día con flexibilidad",
        "lifestyle": "Soy una persona centrada en el equilibrio personal"
    }
    
    result = recommend(user_data)
    
    assert len(result.diets) == 4
    assert len(result.routines) == 4
    assert len(result.articles) == 4
    
    assert "fuerza-silla-de-ruedas" in result.routines
