from flask import Blueprint, render_template

v = Blueprint("default", __name__)


@v.route("/")
def index():
    return render_template("pages/index.html.j2")
