from sqlalchemy import Column, Text
from common.database.models import TableBase


class User(TableBase):
    name = Column(Text)


class Tour(TableBase):
    name = Column(Text)


class Site(TableBase):
    name = Column(Text)


class Partner(TableBase):
    name = Column(Text)
