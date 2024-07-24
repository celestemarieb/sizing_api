from datetime import timedelta
import json

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from sqlalchemy import select

from models.retailer import Size, size_schema
from models.retailer import SizeChart, SizeChartSchema
from models.retailer import Retailer, retailer_schema
from init import bcrypt, db

size_bp = Blueprint("sizes", __name__,url_prefix="/sizes")

# create 
@size_bp.route("/new", methods=["POST"])
def create_size():
    size_fields = size_schema.load(request.json)

    new_size = Size()
    new_size.name = size_fields["name"]
    new_size.bust_measurement = size_fields["bust_measurement"]
    new_size.waist_measurement = size_fields["waist_measurement"]
    new_size.hip_measurement = size_fields["hip_measurement"]
    new_size.sizechart_id = size_fields["sizechart_id"]

    db.session.add(new_size)
    db.session.commit()

    return size_schema.dump(new_size), 201

# update 
#@size_bp.route("/update", methods=["PATCH"])

# read 
#@size_bp.route("/getall",methods=["GET"])
#def get_sizes():
    #size_list = db.session.scalars(select(Size).order_by(Size.id)).all()
    #return size_schema.dump(size_list)

# delete 
#@size_bp.route("/delete",methods=["DELETE"])
#def delete_size():
    # find matching size in database
    #db.session.delete(size)
    #db.session.commit()
    #return size_schema.dump(size), 201 



