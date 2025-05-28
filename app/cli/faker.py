from flask import Blueprint
from app.models.measurement import Measurement
import click
from faker import Faker

faker_cli = Blueprint("faker", __name__)
fake = Faker()


@faker_cli.cli.command("measurement")
@click.argument("number")
def measurement(number):
    from singletons import db

    if not number.isdigit():
        print("Number value is not valid integer")
        return

    n = int(number)
    print(f"Creating {n} fake measurements...")
    measurements = []
    for i in range(n):
        measurements.append(Measurement(value=fake.random_int(min=0, max=9999)))

    db.session.add_all(measurements)

    db.session.commit()
    print(f"{number} measurements added ...")
