from pydantic_settings import BaseSettings, SettingsConfigDict

# Reading the .env configurations
class Settings(BaseSettings):
    DATABASE_URL: str
    DB_NAME: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
