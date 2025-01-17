from flask import Blueprint

from init import db, bcrypt 
from models.user import User
from models.retailer import Retailer
from models.retailer import SizeChart
from models.retailer import Size

db_commands = Blueprint("db",__name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            email="random@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True,
            waist_measurement="189",
            bust_measurement="345",
            hip_measurement="456",
        ),
    ]

    db.session.add_all(users)

    db.session.commit()

    retailers = [
        Retailer(
            id="456",
            name="new",
        ),
    ]

    db.session.add_all(retailers)

    db.session.commit()

    size_charts = [
        SizeChart(
            id="123",
            retailer_id="456",
        )
    ]

    db.session.add_all(size_charts)

    db.session.commit()

    sizes = [
        Size(
            name="M",
            bust_measurement="100",
            waist_measurement="100",
            hip_measurement="100",
            sizechart_id="123",
        )
    ]

    db.session.add_all(sizes)

    db.session.commit()

    print("tables seeded")