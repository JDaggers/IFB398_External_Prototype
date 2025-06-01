from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DBConnection:
    def __init__(self, app=None):
        self.app = app
        self._done_init = False
        self._is_local = (
            False  # This is just for dev purposes to ensure we're using our local db before doing something stupid
        )

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.teardown_appcontext(self.teardown)

        # Set up db connection
        db_user = app.config["DB_USER"]
        db_pass = app.config["DB_PASS"]
        db_host = app.config["DB_HOST"]
        db_name = app.config["DB_NAME"]

        if db_host == "db":
            self._is_local = True

        self.connect(db_user, db_pass, db_host, db_name)

    def connect(self, user, pw, host, db_name):
        # Set pool_recycle to wait_timeout - 1
        self.engine = create_engine(f"mariadb+pymysql://{user}:{pw}@{host}/{db_name}", future=True, pool_pre_ping=True)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine, future=True))

        self.Base = declarative_base()
        self.Base.query = self.session.query_property()
        self.metadata = self.Base.metadata
        self._done_init = True

    def teardown(self, exception=None):
        if self.session:
            self.session.remove()
        return exception
