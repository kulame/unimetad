from fastapi import FastAPI, Response, status
import sqlalchemy
from devtools import debug
import os, json
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Depends
from app.models import MetaTable, get_db, metadata, database
from databases import Database
from datetime import datetime
from app.libs.avro import sign_avro, check_avro, MetaStatus
from app.libs.db import ddl
import urllib
from fastapi.responses import ORJSONResponse

router: APIRouter = APIRouter()







class MetaEventReq(BaseModel):
    name: str
    meta: dict 
    producer: str
    dataframe:str
    dataset:str
    scheme:str
    host:str
    port:int



#TODO 实现元数据写入接口
#TODO 实现元数据读取接口
#TODO 实现元数据查询页面


@router.post("/events/", status_code=status.HTTP_201_CREATED)
async def create_event_meta(req:MetaEventReq, resp:Response) -> dict:
    """
    @api {post} /metatable/ Create Meta Information
    @apiName GetMetaTable
    @apiGroup MetaTable

    @apiParam {String} event  event name.
    @apiParam {Object} meta meta information(avro format).
    @apiParam {String} creator meta creator.
    @apiSuccess {int} status 创建状态.
"""
    mstatus = check_avro(req.meta)
    if mstatus != MetaStatus.SUCCESS:
        return {"status":mstatus}

    signed = sign_avro(req.meta)
    query = "select max(version) from metatable where name=:name"
    res = await database.fetch_one(query=query, values={"name":req.name})
    version = res[0]
    if version is None:
        count = 0
        version = 0 
    else:
        query = "select count(*) from metatable where name=:name and sign=:sign"
        res =  await database.fetch_one(query=query, values={"name":req.name,"sign":signed})
        count = res[0]
        version = version +1
    if count == 0:
        query = "insert into metatable(name,meta,created_at,producer,version,sign, dataframe, dataset, scheme, host, port) values(:name,:meta,:created_at,:producer,:version,:sign,:dataframe, :dataset,:scheme,:host,:port)"
        value = {
            "name": req.name,
            "meta": json.dumps(req.meta),
            "created_at":datetime.now(),
            "producer":req.producer,
            "version":version,
            "sign":signed,
            "dataframe":req.dataframe,
            "dataset":req.dataset,
            "scheme":req.scheme,
            "host":req.host,
            "port":req.port
        }
        res = await database.execute(query, value)
    else:
        resp.status_code = status.HTTP_200_OK
    query = "select id, version from metatable where name=:name and sign=:sign"
    res= await database.fetch_one(query,{"name":req.name,"sign":signed})
    event_id, event_version = res
    data = {"id":event_id, "version":event_version}
    return {'status':0, "data":data}

@router.get("/events/")
async def query_event_meta(name:str, version:int,resp:Response) -> dict:
    name =urllib.parse.unquote(name)
    query = "select id,meta from metatable where name=:name and version=:version"
    data = {"name":name,"version":version}
    res = await database.fetch_one(query=query, values=data)
    if res:
        id, meta = res
        meta = json.loads(meta)
        data = {'id':id, 'meta':meta}
        return {'status':0, "data":data}
    else:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return {"status":1}