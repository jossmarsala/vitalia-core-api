from fastapi import APIRouter

from .score_routes import router as score_router
from .user_routes import router as user_router
from .resource_routes import router as resource_router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(score_router, tags=["Scores"])
router_v1.include_router(user_router, tags=["Users"])
router_v1.include_router(resource_router, tags=["Resources"])
