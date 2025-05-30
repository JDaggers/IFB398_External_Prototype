from flask import Flask
from flask_migrate import Migrate
from singletons import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config/app_config.py")

    # db_user = app.config["DB_USER"]
    # db_pass = app.config["DB_PASS"]
    # db_host = app.config["DB_HOST"]
    # db_name = app.config["DB_NAME"]
    #
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"mariadb+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
    # app.config["SQLALCHEMY_BINDS"] = {
    #     None: f"mariadb+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}",
    #     "proto": f"mariadb+pymysql://{db_user}:{db_pass}@{db_host}/proto",
    # }

    db.init_app(app)

    with app.app_context():
        from app.views import default

        app.register_blueprint(default.v)

        from app.cli.db import db_cli

        app.register_blueprint(db_cli)

        from app.cli.faker import faker_cli

        app.register_blueprint(faker_cli)

        from app.models import measurement  # noqa: F401

    migrate = Migrate(app, db)

    return app
