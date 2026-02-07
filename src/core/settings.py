from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    sentry_dsn: str
    logstash: str
    logstash_transport: str
    logstash_ssl: bool = True
    logstash_port: int = 5044
    event_ttl: int = 30
    project_name: str = 'app'
    min_review_length: int = 1
    max_review_length: int = 5000
    elastic_schema: str = 'http'
    app_start_method: str = 'main:app'
    app_host: str = '0.0.0.0'
    database_url: str = Field(default="mongodb://mongodb:27017")

    class Config:
        env_file = '.env'


settings = Settings()