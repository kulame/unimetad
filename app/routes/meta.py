from fastapi import FastAPI
import sqlalchemy
from devtools import debug
import os
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi_sqlalchemy import db 
from app.models import MetaTable

router: APIRouter = APIRouter()







class MetaEventReq(BaseModel):
    name: str
    meta: dict 
    producer: str



#TODO 实现元数据写入接口
#TODO 实现元数据读取接口
#TODO 实现元数据查询页面


@router.post("/events")
async def create_event_meta(req:MetaEventReq) -> dict:
    """
    @api {post} /metatable/ Create Meta Information
    @apiName GetMetaTable
    @apiGroup MetaTable

    @apiParam {String} event  event name.
    @apiParam {Object} meta meta information(avro format).
    @apiParam {String} creator meta creator.
    @apiSuccess {int} status 创建状态.
"""
    debug(req)
    result = db.session.query(MetaTable).all()
    debug(result)

    return {"Hello": "World"}
