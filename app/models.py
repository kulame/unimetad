from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData
from app.config import get_settings
import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from devtools import debug
from loguru import logger
#TODO implement test database generate



def get_db() -> databases.Database:
    settings = get_settings()
    database_url = settings.DATABASE_URL
    logger.info("connect {url}...".format(url=database_url))
    database = databases.Database(database_url, min_size=10, max_size=200)
    return database

database = get_db()

metadata = MetaData()



MetaTable = Table(
    'metatable', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True, index=True),
    Column('name', String(200)),
    Column('meta', JSON),
    Column('created_at', DateTime),
    Column('producer', String(200)),
    Column("version",Integer),
    Column("sign",String(200)),
    Column("dataframe", String(200)),
    Column("dataset", String(200)),
    Column("scheme", String(200)),
    Column("host", String(200)),
    Column("port", Integer)
)

