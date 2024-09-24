
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    test: str

    model_config = SettingsConfigDict(env_file='../.env')


settings = Settings()

