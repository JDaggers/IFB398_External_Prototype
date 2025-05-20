import sys
sys.path.append("/home/app/prototype")

from app import create_app
from app.models.test import Measurement
from singletons import db

app = create_app()

with app.app_context():
    db.session.add_all([
        Measurement(value=10.5),
        Measurement(value=5.2),
        Measurement(value=7.8),
        Measurement(value=15.0),
        Measurement(value=3.3),
    ])
    db.session.commit()
    print("Test data added.")
