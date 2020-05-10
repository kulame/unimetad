from fastapi import FastAPI

from app.libs.http import setup_session  # type: ignore
from app.libs.http import teardown_session
from app.routes.api import router
from app.config import get_settings
from app.models import database



def get_app():
    settings = get_settings()
    app = FastAPI(
        title="unimetad API",
        description=("unimetad API"),
        version="0.1.0",
        docs_url="/",
        redoc_url="/docs",
        on_startup=[setup_session],
        on_shutdown=[teardown_session],
    )
    
    database_url = settings.DATABASE_URL
    app.include_router(router, prefix="/api", tags=["api"])
    return app

app = get_app()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

