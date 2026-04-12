"""
Scoring engine — weighted dot-product scoring.

Computes a deterministic score for each resource based on how many of
the user's features overlap with the resource's features, weighted by
the resource's per-feature importance weights.

Penalty logic ensures resources with hard requirements (penalty_if_missing)
are deprioritized when the user lacks critical features.
"""

import logging
from typing import Set

from .catalog import Resource

logger = logging.getLogger(__name__)

# Penalty applied when a resource has a "penalty_if_missing" feature
# that is NOT present in the user's profile.
MISSING_PENALTY = -10.0


def score_resource(user_features: Set[str], resource: Resource) -> float:
    """
    Compute a weighted score for a single resource against user features.
    
    Score = sum(resource.weights[f] for f in user_features ∩ resource.features)
            + MISSING_PENALTY for each f in resource.penalty_if_missing - user_features
    
    This is fully deterministic: same inputs always produce the same output.
    
    Args:
        user_features: Set of feature tags extracted from user questionnaire.
        resource: A Resource from the catalog.
    
    Returns:
        float score. Higher is better. Can be negative if penalties dominate.
    """
    score = 0.0

    # Positive scoring: weighted dot-product on feature intersection
    matching_features = user_features & resource.features
    for feature in matching_features:
        weight = resource.weights.get(feature, 1.0)
        score += weight

    # Negative scoring: penalty for missing required features
    missing_required = resource.penalty_if_missing - user_features
    for feature in missing_required:
        score += MISSING_PENALTY

    return score


def score_all(user_features: Set[str], resources: list[Resource]) -> list[tuple[Resource, float]]:
    """
    Score and rank a list of resources for a given user profile.
    
    Returns resources sorted by score descending (best first).
    Ties are broken by resource ID for deterministic ordering.
    
    Args:
        user_features: Set of feature tags from user questionnaire.
        resources: List of Resource objects to score.
    
    Returns:
        List of (Resource, score) tuples, sorted by score descending.
    """
    scored = []
    for resource in resources:
        s = score_resource(user_features, resource)
        scored.append((resource, s))

    # Sort by score descending, then by ID ascending for deterministic tiebreaking
    scored.sort(key=lambda x: (-x[1], x[0].id))

    if logger.isEnabledFor(logging.DEBUG):
        for resource, s in scored:
            logger.debug(f"  [{resource.category}] {resource.id}: {s:.1f}")

    return scored
