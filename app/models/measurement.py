from sqlalchemy import Column, Float
from common.database.models import TableBase

class Measurement(TableBase):
    value = Column(Float, nullable=False)
