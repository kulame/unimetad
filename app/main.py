from fastapi import FastAPI

from app.libs.http import setup_session  # type: ignore
from app.libs.http import teardown_session
from app.routes.api import router

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
