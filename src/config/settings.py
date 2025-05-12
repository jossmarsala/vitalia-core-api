from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API
    PORT: int = 8000
    DEV: Bool = True

    class Config:
        env_file = ".env"
        