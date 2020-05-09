from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData



metadata = MetaData()

MetaTable = Table(
    'metatable', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True, index=True),
    Column('name', String(200)),
    Column('meta', JSON),
    Column('created_at', DateTime),
    Column('producer', String(200))
)