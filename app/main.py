from fastapi import FastAPI

from app.libs.http import setup_session  # type: ignore
from app.libs.http import teardown_session
from app.routes.api import router
from app.config import get_settings
import databases
from app.models import database
from loguru import logger

def get_app():    
    app = FastAPI(
        title="unimetad API",
        description=("unimetad API"),
        version="0.1.0",
        docs_url="/",
        redoc_url="/docs",
        on_startup=[setup_session],
        on_shutdown=[teardown_session],
    )
    app.include_router(router, prefix="/api", tags=["api"])
    return app

app = get_app()

@app.on_event("startup")
async def startup():
    await database.connect()
    logger.success("connect database success")


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    logger.success("disconnect database success")

