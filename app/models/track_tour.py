from sqlalchemy import Column, Float, Binary, Date
from common.database.models import TableBase


class TrackTour(TableBase):
    user_id = Column(Binary(16))
    tour_id = Column(Binary(16))
    departure_date = Column(Date)
    price = Column(Float(precision=2, asdecimal=True))
