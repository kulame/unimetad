from fastapi import APIRouter

from app.routes import demo

router: APIRouter = APIRouter()
router.include_router(demo.router, tags=["demo"], prefix="/demo")
