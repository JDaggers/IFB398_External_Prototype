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
    print(f"[Chart Debug] Min: {min_val}, Max: {max_val}")
    return render_template("pages/index.html.j2", min_val=min_val, max_val=max_val)


@v.route("/analytics")
def show_data():
    fact = get_fact()
    return render_template("pages/analytics.html.j2", data=fact)

@v.route("/line-graph")
def show_line_graph():
    return render_template("pages/line_graph.html.j2")

@v.route("/api/measurements")
def get_measurements():
    measurements = db.session.query(Measurement).all()
    values = [m.value for m in measurements]
    labels = [f"Point {i+1}" for i in range(len(values))]
    return {"labels": labels, "values": values}

