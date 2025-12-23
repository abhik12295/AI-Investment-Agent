from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Investment Agent"
    ENV : str = "dev"
    CACHE_TTL: int = 3600  # Cache time-to-live in seconds

settings = Settings()