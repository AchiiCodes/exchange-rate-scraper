"""crawl/crawl/models.py"""
from sqlalchemy import Column, String, Double, DateTime, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from crawl import settings

DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL.create(**settings.DATABASE))


def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    DeclarativeBase.metadata.create_all(engine)


class PottchangeItem(DeclarativeBase):
    """
    Defines the pottchange model
    """

    __tablename__ = "pottchange"

    land_code = Column("land_code", String, primary_key=True)
    created_date = Column(
        "created_date", DateTime, default=datetime.utcnow, primary_key=True
    )
    sell_per_100 = Column("sell_per_100", Double)
    buy_per_100 = Column("buy_per_100", Double)
    sell_per_euro = Column("sell_per_euro", Double)
    buy_per_euro = Column("buy_per_euro", Double)
