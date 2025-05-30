from sqlalchemy import Column, Float, Date, String, Boolean, DateTime, JSON
from common.database.models import TableBase
from common.database.guid import GUID


class TrackTour(TableBase):
    user_id = Column(GUID)
    tour_id = Column(GUID)
    partner_id = Column(GUID)
    site_id = Column(GUID)
    departure_date = Column(Date)
    price = Column(Float(precision=2, asdecimal=True))
    currency = Column(String(3))
    booked = Column(Boolean)


class TrackUser(TableBase):
    partner_id = Column(GUID)
    site_id = Column(GUID)
    ip = Column(String(128))
    country = Column(String(128))


class TrackSearch(TableBase):
    user_id = Column(GUID)
    partner_id = Column(GUID)
    site_id = Column(GUID)
    when = Column(DateTime)
    results = Column(Boolean)
    filters = Column(JSON)
