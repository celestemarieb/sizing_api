from flask import Blueprint

from init import db, bcrypt 
from models.user import User

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
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True,
            waist_measurement="189",
            bust_measurement="345",
            hip_measurement="456",
        ),
    ]

    db.session.add_all(users)

    db.session.commit()

    print("tables seeded")