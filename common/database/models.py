from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
import timeflake
import re

from common.database import GUID, uuid

db = SQLAlchemy()

class TableBase(db.Model):
    """
    Base model class that all others should inherit from.
    It includes:
    - UUID primary key
    - language code
    - created_at / updated_at
    """
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    id = Column(GUID, primary_key=True, default=uuid)
    language = Column(String(5), default='en')
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def fields(cls):
        return [col.name for col in cls.__table__.columns]

    def values(self, bin_ids=False):
        if bin_ids:
            values = []
            for col in self.__table__.columns:
                values.append(getattr(self, col.name))
                if isinstance(col.type, GUID) and values[-1]:
                    values[-1] = timeflake.parse(from_hex=values[-1]).bytes
            return values
        return [getattr(self, field) for field in self.fields()]

    def asdict(self):
        return {field: getattr(self, field) for field in self.fields()}

    def __repr__(self):
        _id = self.id.hex if isinstance(self.id, timeflake.Timeflake) else self.id
        return f'<{self.__class__.__name__} {_id}>'
