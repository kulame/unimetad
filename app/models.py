from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData
from app.config import get_settings
import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#TODO implement test database generate
settings = get_settings()
DATABASE_URL = settings.DATABASE_URL
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


metadata = MetaData()



MetaTable = Table(
    'metatable', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True, index=True),
    Column('name', String(200)),
    Column('meta', JSON),
    Column('created_at', DateTime),
    Column('producer', String(200))
)

metadata.create_all(engine)
