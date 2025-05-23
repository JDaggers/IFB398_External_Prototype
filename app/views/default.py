from flask import Blueprint, render_template
from app.ai import get_fact
from app.models.measurement import Measurement
from sqlalchemy import func
from singletons import db


v = Blueprint("default", __name__)


@v.route("/")
def index():
    min_val = db.session.query(func.min(Measurement.value)).scalar()
    max_val = db.session.query(func.max(Measurement.value)).scalar()

    chart_data = [
        {
        "id": "chart1",
        "type": "bar",
        "label": "Measurements",
        "labels": ["Min", "Max"],
        "data": [min_val, max_val],
        "backgroundColor": ["#1abc9c", "#3498db", "#f39c12"]
        },
        {
            "id": "chart2",
            "type": "line",
            "label":"Measurements",
            "labels": ["min", "max"],
            "data": [min_val, max_val]
        }
    ]

    return render_template("pages/index.html.j2", min_val=min_val, max_val=max_val, chart_data=chart_data)



@v.route("/analytics")
def show_data():
    fact = get_fact()
    return render_template("pages/analytics.html.j2", data=fact)

