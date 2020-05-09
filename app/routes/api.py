from fastapi import APIRouter

from app.routes import demo, meta

router: APIRouter = APIRouter()
router.include_router(demo.router, tags=["demo"], prefix="/demo")
router.include_router(meta.router, tags=['meta'], prefix='/meta')
