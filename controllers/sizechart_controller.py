from datetime import timedelta
import json

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from sqlalchemy import select

from models.retailer import SizeChart, sizechart_schema
from models.retailer import Retailer, retailer_schema
from init import bcrypt, db

sizechart_bp = Blueprint("sizecharts", __name__,url_prefix="/sizecharts")

# create 
@sizechart_bp.route("/new", methods=["POST"])
def create_sizechart():
    sizechart_fields = sizechart_schema.load(request.json)

    new_sizechart = SizeChart()
    new_sizechart.id = sizechart_fields["id"]
    new_sizechart.retailer_id = sizechart_fields["retailer_id"]

    db.session.add(new_sizechart)
    db.session.commit()

    return sizechart_schema.dump(new_sizechart), 201

# update 

# read 

# delete 