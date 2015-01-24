from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_ios_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Ios(DeclarativeBase):
    __tablename__ = "ios"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    url = Column('url', String(200))
    pic = Column('pic',String(200))
