from sqlalchemy.dialects import mysql
from sqlalchemy.schema import CreateTable
from sqlalchemy import Table

def ddl(table:Table):
    sql = CreateTable(table).compile(dialect=mysql.dialect())
    return sql
