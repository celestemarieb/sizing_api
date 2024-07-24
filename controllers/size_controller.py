from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token

from models.user import User, user_schema
from init import bcrypt, db

size_bp = Blueprint("sizes", __name__,url_prefix="/sizes")

# create 
@size_bp.route("/sizes", methods=["POST"])
def register_size():
    body_data = request.get_json()
    size = Size(
        name=body_data.get("name")
        bust_measurement=body_data.get("bust_measurement")
        waist_measurement=body_data.get("waist_measurement")
        hip_measurement=body_data.get("hip_measurement")
    )

    db.session.add(size)
    db.session.commit()

    return size_schema.dump(size), 201

# update 

# read 
@size_bp.route("/sizes",methods=["GET"])
    def get_sizes():
        sizes_list = Size.query.all()
        result = sizes_schema.dump(sizes_list)
        return jsonify(result)

# delete 
@size_bp.route("/sizes",methods=["DELETE"])
def delete_size():
        


