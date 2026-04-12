"""
Vitalia Recommendation Engine

Deterministic, weighted, in-memory recommendation system.
Matches user questionnaire answers to the best-fitting resources
across three categories: diets, routines, and articles.
"""

from .engine import recommend, RecommendationResult

__all__ = ["recommend", "RecommendationResult"]
