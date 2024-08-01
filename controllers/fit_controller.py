from datetime import timedelta
import json

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from sqlalchemy import select, and_

from models.retailer import Size, size_schema, sizes_schema
from models.retailer import SizeChart, SizeChartSchema
from models.retailer import Retailer, retailer_schema
from models.user import User, user_schema, users_schema
from init import db

fit_bp = Blueprint("fit", __name__,url_prefix="/fit")

# GET /fit/find - Find A Good Fit (a size which matches the users dimensions) (7)
@fit_bp.route("/find/<id>", methods=["GET"])
def find_fit(id):
    user_bust = db.session.execute(
        select(User.bust_measurement)
        .where(User.id == id)
    )
    waist_measurement = db.session.execute(
        select(User.waist_measurement)
        .where(User.id == id)
    )
    hip_measurement = db.session.execute(
        select(User.hip_measurement)
        .where(User.id == id)
    )
    matching_sizes =  db.session.query(Size).filter(Size.bust_measurement == user_bust, Size.waist_measurement == waist_measurement, Size.hip_measurement == hip_measurement)
    result = size_schema.dump(matching_sizes)
    return jsonify(result), 200

