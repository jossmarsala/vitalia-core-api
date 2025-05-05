from fastapi import FastAPI

api_server = FastAPI(
    description="API responsable de ofrecer recomendaciones personalizadas de recursos de bienestar en la plataforma Vitalia Selfcare.",
    version="0.1.0",
    title="Vitalia Core")
