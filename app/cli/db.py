from flask import Blueprint

db_cli = Blueprint("db", __name__)


@db_cli.cli.command("init")
def init():
    from singletons import db

    db.metadata.create_all(bind=db.engine)
