"""
Recommendation engine — top-level orchestrator.

Wires together feature extraction, the resource catalog, and the scoring
engine to produce a final set of recommendations (top 4 per category).
"""

import logging
from dataclasses import dataclass, field

from .features import extract_user_features
from .catalog import DIETS, ROUTINES, ARTICLES
from .scoring import score_all

logger = logging.getLogger(__name__)

# Number of recommendations per category
TOP_N = 4


@dataclass
class RecommendationResult:
    """Final recommendation output — 4 resource slugs per category."""
    diets: list[str] = field(default_factory=list)
    routines: list[str] = field(default_factory=list)
    articles: list[str] = field(default_factory=list)


def _pick_top(scored: list[tuple], n: int, category_name: str) -> list[str]:
    """
    Pick the top N resource IDs from a scored list.
    
    Graceful fallback: if fewer than N resources have positive scores,
    include the next-best resources anyway (better to recommend something
    than nothing). Only resources with score > MINIMUM_SCORE are included,
    but if we can't reach N items, we fill from the top of whatever remains.

    Diversity: limits how many resources sharing the same dominant feature
    can appear in the final selection (MAX_SAME_DOMINANT). This prevents
    recommending 3 "busy schedule" diets when the user also has sleep issues.
    
    Args:
        scored: List of (Resource, score) tuples, already sorted by score desc.
        n: Number of items to pick.
        category_name: For logging only.
    
    Returns:
        List of resource ID strings, length exactly n (or fewer if
        the entire category has fewer than n resources).
    """
    # Take top N, even if some scores are 0 or slightly negative
    # (only hard-penalized resources will have very negative scores)
    MINIMUM_THRESHOLD = -5.0
    # Max resources sharing the same dominant feature in one recommendation set
    MAX_SAME_DOMINANT = 2

    def _dominant_feature(resource) -> str:
        """Return the feature with the highest weight for this resource."""
        if not resource.weights:
            return resource.id
        return max(resource.weights, key=resource.weights.get)

    selected = []
    dominant_counts: dict[str, int] = {}

    for resource, score in scored:
        if len(selected) >= n:
            break
        if score <= MINIMUM_THRESHOLD:
            continue

        dominant = _dominant_feature(resource)
        current_count = dominant_counts.get(dominant, 0)
        if current_count >= MAX_SAME_DOMINANT:
            continue  # skip to maintain diversity

        selected.append(resource.id)
        dominant_counts[dominant] = current_count + 1

    # If we still don't have enough, relax diversity and fill from remaining
    if len(selected) < n:
        for resource, score in scored:
            if resource.id not in selected:
                selected.append(resource.id)
            if len(selected) >= n:
                break

    logger.info(
        f"Recommendations [{category_name}]: "
        f"{selected} (from {len(scored)} candidates)"
    )
    return selected[:n]


def recommend(user_data: dict) -> RecommendationResult:
    """
    Generate personalized recommendations for a user.
    
    This is the main entry point of the recommendation engine.
    
    Pipeline:
        1. Extract feature tags from raw questionnaire answers
        2. Score all resources in each category using weighted dot-product
        3. Pick top 4 per category with graceful fallback
    
    Args:
        user_data: Dict containing questionnaire answers, matching the
                   keys from the API user schema (disability, physicalActivity,
                   diet, restrictions, wellbeingGoals, obstacles, sleepQuality,
                   stressLevel, dailyRoutine, lifestyle).
    
    Returns:
        RecommendationResult with top 4 diets, routines, and articles.
    """
    logger.info("Starting recommendation computation")

    # Step 1: Extract structured features from raw answers
    user_features = extract_user_features(user_data)
    logger.info(f"User features ({len(user_features)}): {user_features}")

    # Step 2: Score all resources per category
    scored_diets = score_all(user_features, DIETS)
    scored_routines = score_all(user_features, ROUTINES)
    scored_articles = score_all(user_features, ARTICLES)

    # Step 3: Pick top N per category
    result = RecommendationResult(
        diets=_pick_top(scored_diets, TOP_N, "diets"),
        routines=_pick_top(scored_routines, TOP_N, "routines"),
        articles=_pick_top(scored_articles, TOP_N, "articles"),
    )

    logger.info(f"Recommendation complete: {result}")
    return result
