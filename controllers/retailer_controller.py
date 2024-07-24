from datetime import timedelta
import json

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from sqlalchemy import select

from models.user import User, user_schema
from models.retailer import Size, size_schema
from models.retailer import SizeChart, SizeChartSchema
from models.retailer import Retailer, retailer_schema
from init import bcrypt, db

retailer_bp = Blueprint("retailer", __name__,url_prefix="/retailer")

# create 

@retailer_bp.route("/new", methods=["POST"])
def create_retailer():
    retailer_fields = retailer_schema.load(request.json)

    new_retailer = Retailer()
    new_retailer.id = retailer_fields["id"]
    new_retailer.name = retailer_fields["name"]

    db.session.add(new_retailer)
    db.session.commit()

    return retailer_schema.dump(new_retailer), 201

# update 

# read 

# delete 