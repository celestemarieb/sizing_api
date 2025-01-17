from marshmallow import fields
from init import db, ma 

class User(db.Model):
    __tablename__ = "users"

    # primary key 
    id = db.Column(db.Integer, primary_key=True)
    # attributes 
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    waist_measurement = db.Column(db.String)
    hip_measurement = db.Column(db.String)
    bust_measurement = db.Column(db.String)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password","is_admin","waist_measurement","hip_measurement","bust_measurement")

user_schema = UserSchema(exclude=["password"])

users_schema = UserSchema(many=True, exclude=["password"])