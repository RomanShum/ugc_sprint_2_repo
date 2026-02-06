from contextlib import asynccontextmanager
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from api.urls import router
from models.like import Like
from models.favorite import Favorite
from models.review import Review
from core.settings import Settings
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
import logstash

settings = Settings()

@asynccontextmanager
async def lifespan(_: FastAPI):
    dsn = settings.sentry_dsn
    if dsn:
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            integrations=[FastApiIntegration()],
            send_default_pii=True
        )
    client = AsyncIOMotorClient(settings.database_url)
    await init_beanie(database=client.db_name, document_models=[Like, Favorite, Review])
    yield
    client.close()


app = FastAPI(
    lifespan=lifespan,
    title='App',
    docs_url='/docs',
    openapi_url='/api/openapi.json',
    description='App Service',
    version='0.1.0',
)

app.include_router(router)