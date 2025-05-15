import logging

from fastapi import FastAPI

from .routes import api_router
from .config.logger import configure_logging


configure_logging()

logger = logging.getLogger(__name__)

api_server = FastAPI(
    description="API responsable de ofrecer recomendaciones personalizadas de recursos de bienestar en la plataforma Vitalia Selfcare.",
    version="0.1.0",
    title="Vitalia Core")

@api_server.get("/")
async def root():
    return {"message": "FastAPI corriendo"}

api_server.include_router(api_router)
logger.info("API Inicializada")