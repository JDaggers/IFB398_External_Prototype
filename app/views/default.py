from flask import Blueprint, render_template
from app.ai import get_fact

v = Blueprint("default", __name__)


@v.route("/")
def index():
    return render_template("pages/index.html.j2")

@v.route("/analytics")
def show_data():
    fact = get_fact()
    return render_template("pages/analytics.html.j2", data=fact)