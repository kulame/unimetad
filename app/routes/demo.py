from typing import Dict

from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get("/test")
async def read_demo_root() -> Dict[str, str]:
    """
        @api {get} /api/demo/test for test
        @apiName test
        @apiGroup demo

        @apiSuccess {string} Hello for test
    """
    return {"Hello": "World"}
