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

# POST /sizes/new - Create a New Size (3)
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

# PUT /sizes/update - Update a Size (4)
@size_bp.route("/update", methods=["PATCH"])
def update_size():
    return {"message": "Placeholder"}, 200

# DELETE /sizes/delete - Delete a Size (5)
@size_bp.route("/delete",methods=["DELETE"])
def delete_size():
    size_fields = size_schema.load(request.json)
    new_size = Size()
    new_size.id = size_fields["id"]
    size = db.session.execute(db.select(Size).filter_by(id=new_size.id))

    db.session.delete(size)
    db.session.commit()

    return {"message": "Size deleted"}, 200

# GET /sizes/all - Display All Sizes (6)
@size_bp.route("/getall",methods=["GET"])
def get_sizes():
    size_list = db.session.scalars(select(Size).order_by(Size.id)).all()
    return size_schema.dump(size_list)



