from sqlalchemy import Column, Numeric, String
from common.database.models import TableBase


class Test(TableBase):
    test = Column(Numeric(15))
    test_2 = Column(Numeric(5))
    test_3 = Column(Numeric(5))
    test_4 = Column(String(100))
