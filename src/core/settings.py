from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    project_name: str = 'app'
    elastic_schema: str = 'http'
    film_cache_expire_in_seconds: int = 60 * 5
    app_start_method: str = 'main:app'
    app_host: str = '0.0.0.0'
    database_url: str = Field(default="mongodb://mongodb:27017")

    class Config:
        env_file = '.env'


settings = Settings()