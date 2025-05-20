from flask import Flask
from flask_migrate import Migrate
from singletons import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config/app_config.py")

    db.init_app(app)

    with app.app_context():
        from app.views import default

        app.register_blueprint(default.v)

        from app.cli.db import db_cli

        app.register_blueprint(db_cli)

        from app.models import test 
        
    migrate = Migrate(app, db)

    return app
