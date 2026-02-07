from contextlib import asynccontextmanager
from beanie import init_beanie
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from api.urls import router
from models.like import Like
from models.favorite import Favorite
from models.review import Review
from core.settings import Settings
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from logstash_async.handler import AsynchronousLogstashHandler
import logging
import uuid

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

logger = logging.getLogger('fastapi')
logger.setLevel(logging.INFO)

logstash_handler = AsynchronousLogstashHandler(
    host=settings.logstash,
    port=settings.logstash_port,
    database_path=None,
    transport=settings.logstash_transport,
    ssl_enable=settings.logstash_ssl,
    enable=True,
    event_ttl=30,
)
logger.addHandler(logstash_handler)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = request.headers.get('X-Request-Id') or str(uuid.uuid4())

    try:
        response = await call_next(request)
        logger.info('Request', extra={
            'request_id': request_id,
            'status_code': response.status_code,
            'method': request.method,
        })

        response.headers['X-Request-Id'] = request_id

        return response

    except Exception as e:
        logger.error('Request failed', extra={
            'request_id': request_id,
            'error': str(e),
            'method': request.method,
            'path': request.url.path,
        }, exc_info=True)
        raise

app.include_router(router)