from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData
from app.config import get_settings
import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from devtools import debug
#TODO implement test database generate



def get_db() -> databases.Database:
    settings = get_settings()
    database_url = settings.DATABASE_URL
    database = databases.Database(database_url, min_size=100, max_size=1000)
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
    Column("sign",String(200))
)

