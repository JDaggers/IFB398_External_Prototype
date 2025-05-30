from sqlalchemy import Column, Float, BINARY, Date, String, Boolean, DateTime, JSON
from common.database.models import TableBase


class TrackTour(TableBase):
    user_id = Column(BINARY(16))
    tour_id = Column(BINARY(16))
    partner_id = Column(BINARY(16))
    site_id = Column(BINARY(16))
    departure_date = Column(Date)
    price = Column(Float(precision=2, asdecimal=True))
    currency = Column(String(3))
    booked = Column(Boolean)


class TrackUser(TableBase):
    partner_id = Column(BINARY(16))
    site_id = Column(BINARY(16))
    ip = Column(String(128))
    country = Column(String(128))


class TrackSearch(TableBase):
    user_id = Column(BINARY(16))
    partner_id = Column(BINARY(16))
    site_id = Column(BINARY(16))
    when = Column(DateTime)
    results = Column(Boolean)
    filters = Column(JSON)
