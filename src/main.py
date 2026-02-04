from contextlib import asynccontextmanager
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient,AsyncIOMotorDatabase
from api.urls import router
from models.like import Like
from models.favorite import Favorite
from models.review import Review
from core.settings import Settings

settings = Settings()

@asynccontextmanager
async def lifespan(_: FastAPI):
    client: AsyncIOMotorClient[str] = AsyncIOMotorClient(settings.database_url)
    db: str = client.db_name
    await init_beanie(database=db, document_models=[Like, Favorite, Review])
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