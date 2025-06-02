from flask import Blueprint, render_template
from app.ai import get_fact
from app.models.tracking import TrackSearch, TrackTour, TrackUser
from app.models.objects import Site, User, Partner, Tour
from sqlalchemy import func
from singletons import db
from calendar import month_name


v = Blueprint("default", __name__)


@v.route("/")
def index():
    searches_by_month = (
        db.session.query(func.month(TrackSearch.when), func.count(TrackSearch.id))
        .group_by(func.month(TrackSearch.when))
        .order_by(func.month(TrackSearch.when))
        .all()
    )
    tours_by_dep_date = (
        db.session.query(func.month(TrackTour.departure_date), func.count(TrackTour.id))
        .group_by(func.month(TrackTour.departure_date))
        .order_by(func.month(TrackTour.departure_date))
        .all()
    )
    users_by_country = (
        db.session.query(TrackUser.country, func.count(TrackUser.id))
        .group_by(TrackUser.country)
        .order_by(func.count(TrackUser.id).desc())
        .limit(10)
        .all()
    )

    users_by_site = (
        db.session.query(Site.name, func.count(TrackUser.id))
        .join(Site, Site.id == TrackUser.site_id)
        .group_by(Site.id)
        .all()
    )

    chart_data = [
        {
            "id": "chart1",
            "type": "line",
            "title": "Tracked Searches by Month",
            "datasetLabel": "Tracked Searches",
            "yLabel": "Tracked Searches",
            "labels": [month_name[month] for month, searches in searches_by_month],
            "data": [searches for month, searches in searches_by_month],
            "backgroundColor": None,
        },
        {
            "id": "chart2",
            "type": "pie",
            "title": "Tracked Users by Country - Top 10",
            "datasetLabel": "Tracked Users",
            "labels": [country for country, users in users_by_country],
            "data": [users for country, users in users_by_country],
            "backgroundColor": None,
        },
        {
            "id": "chart3",
            "type": "pie",
            "title": "Tracked Users by Site",
            "datasetLabel": "Tracked Users",
            "yLabel": "Tracked Users",
            "labels": [name for name, users in users_by_site],
            "data": [users for name, users in users_by_site],
            "backgroundColor": None,
        },
        {
            "id": "chart4",
            "type": "bar",
            "title": "Tracked Tours by Month of Departure",
            "datasetLabel": "Tracked Tours",
            "yLabel": "Tracked Tours",
            "labels": [month_name[month] for month, tours in tours_by_dep_date],
            "data": [tours for month, tours in tours_by_dep_date],
            "backgroundColor": None,
        },
    ]

    return render_template("pages/index.html.j2", chart_data=chart_data)


@v.route("/analytics")
def show_data():
    fact = get_fact()
    return render_template("pages/analytics.html.j2", data=fact)

@v.route("/kpi", endpoint="kpi_dashboard")
def kpi_dashboard():

    user_count = db.session.query(User).count()
    site_count = db.session.query(Site).count()
    partner_count = db.session.query(Partner).count()
    tour_count = db.session.query(Tour).count()
    search_count = db.session.query(TrackSearch).count()

    return render_template("pages/kpi.html.j2", kpis={
        "Users": user_count,
        "Sites": site_count,
        "Partners": partner_count,
        "Tours": tour_count,
        "Searches": search_count,
    })