from flask import Blueprint
from app.models.measurement import Measurement
from app.models.objects import User, Tour, Site, Partner
from app.models.tracking import TrackSearch, TrackTour, TrackUser
import click
from faker import Faker
from faker.providers import internet, person, company, date_time, currency, python, address, misc

faker_cli = Blueprint("faker", __name__)
fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)
fake.add_provider(company)
fake.add_provider(date_time)
fake.add_provider(currency)
fake.add_provider(python)
fake.add_provider(address)
fake.add_provider(misc)


def create_measurment():
    return Measurement(value=fake.random_int(min=0, max=9999))


def create_user():
    return User(name=fake.name())


def create_tour():
    return Tour(name=fake.bs())


def create_site():
    return Site(name=fake.domain_name())


def create_partner():
    return Partner(name=fake.company())


def create_track_tour(users, tours, partners, sites):
    assert len(users) > 0
    assert len(tours) > 0
    assert len(partners) > 0
    assert len(sites) > 0
    return TrackTour(
        user_id=fake.random_element(users),
        tour_id=fake.random_element(tours),
        partner_id=fake.random_element(partners),
        site_id=fake.random_element(sites),
        departure_date=fake.date_object(),
        price=fake.pyfloat(right_digits=2, positive=True, min_value=100.00, max_value=50000.00),
        currency=fake.currency_code(),
        booked=fake.pybool(),
    )


def create_track_user(users, tours, partners, sites):
    assert len(partners) > 0
    assert len(sites) > 0
    return TrackUser(
        partner_id=fake.random_element(partners),
        site_id=fake.random_element(sites),
        ip=fake.ipv4(),
        country=fake.country(),
    )


def create_track_search(users, tours, partners, sites):
    assert len(users) > 0
    assert len(partners) > 0
    assert len(sites) > 0
    json_fields = [
        ("search", "bs"),
        ("price-range", "pystr_format", {"string_format": "{{random_int}}-{{random_int}}"}),
        ("duration", "pystr_format", {"string_format": "{{random_int}}-{{random_int}}"}),
    ]
    return TrackSearch(
        user_id=fake.random_element(users),
        partner_id=fake.random_element(partners),
        site_id=fake.random_element(sites),
        results=fake.pybool(),
        when=fake.date_time(),
        filters=fake.json(json_fields, num_rows=1),
    )


tables = {
    "measurement": create_measurment,
    "user": create_user,
    "tour": create_tour,
    "site": create_site,
    "partner": create_partner,
    "track_user": create_track_user,
    "track_tour": create_track_tour,
    "track_search": create_track_search,
}

tracking_tables = ["track_user", "track_search", "track_tour"]


@faker_cli.cli.command("create")
@click.argument("table", type=click.Choice(tables.keys(), case_sensitive=False))
@click.argument("number", type=click.IntRange(min=1))
def create(table, number):
    """
    Create fake rows in a table using faker.
    """
    from singletons import db

    n = number
    if table not in tables.keys():
        print(f'"{table}" is not a valid object')
        return

    if table in tracking_tables:
        tracking = True
        users = db.session.query(User.id).all()
        users = [user[0] for user in users]
        tours = db.session.query(Tour.id).all()
        tours = [tour[0] for tour in tours]
        sites = db.session.query(Site.id).all()
        sites = [site[0] for site in sites]
        partners = db.session.query(Partner.id).all()
        partners = [partner[0] for partner in partners]
        if len(users) == 0 or len(tours) == 0 or len(sites) == 0 or len(partners) == 0:
            print("No entries in (one of) user, tour, site, partner")
            return
    else:
        tracking = False

    print(f"Creating {n} fake {table}('s)...")
    rows = []
    create_func = tables[table]
    if tracking:
        for i in range(n):
            rows.append(create_func(users, tours, sites, partners))
    else:
        for i in range(n):
            rows.append(create_func())

    db.session.add_all(rows)

    db.session.commit()
    print(f"{n} {table}('s) added ...")


@faker_cli.cli.command("tracking_dataset")
def dataset():
    """
    Populate tracking tables aswell as the object tables they rely on.
    """
    print("""
Creating Dataset of:
1000 Users
10 sites
300 Tours
10 Partners
1500 track_user rows
4000 track_tour rows
2500 track_search rows
    """)
    ctx = click.Context(create)
    ctx.invoke(create, table="user", number=1000)
    ctx.invoke(create, table="site", number=10)
    ctx.invoke(create, table="tour", number=300)
    ctx.invoke(create, table="partner", number=10)
    ctx.invoke(create, table="track_user", number=1500)
    ctx.invoke(create, table="track_tour", number=4000)
    ctx.invoke(create, table="track_search", number=2500)
    print("Created Dataset!")
