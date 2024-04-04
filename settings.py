from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Chat fastapi"
    db_url: str

    model_config = SettingsConfigDict(env_file=".env")
