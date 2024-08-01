from datetime import timedelta
import json

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from sqlalchemy import select

from models.retailer import Size, sizes_schema, size_schema
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
@size_bp.route("/update", methods=["PUT"])
def update_size():
    size_fields = size_schema.load(request.json)

    new_size = Size()
    new_size.id = size_fields["id"]
    new_size = Size.query.get(new_size.id)

    new_size.name = size_fields["name"]
    new_size.bust_measurement = size_fields["bust_measurement"]
    new_size.waist_measurement = size_fields["waist_measurement"]
    new_size.hip_measurement = size_fields["hip_measurement"]
    new_size.sizechart_id = size_fields["sizechart_id"]

    db.session.commit()

    return size_schema.dump(new_size), 200

# DELETE /sizes/delete/<id> - Delete a Size (5)
@size_bp.route("/delete/<id>",methods=["DELETE"])
def delete_size(id):
    size = Size.query.get(id)
    db.session.delete(size)
    db.session.commit()
    return {"message": "Size deleted"}, 200

# GET /sizes/get - Display All Sizes (6)
@size_bp.route("/get",methods=["GET"])
def get_sizes():
    all_sizes = Size.query.all()
    result = sizes_schema.dump(all_sizes)
    return jsonify(result)



