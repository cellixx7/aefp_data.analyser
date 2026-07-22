from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Portal AEFP"
    DEBUG: bool = True
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()