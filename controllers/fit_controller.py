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
from models.user import User, user_schema
from init import bcrypt, db

fit_bp = Blueprint("fit", __name__,url_prefix="/fit")

# GET /fit/find - Find A Good Fit (a size which matches the users dimensions) (7)
@fit_bp.route("/find", methods=["POST"])
def find_fit():
    #user_id = user_schema.load(request.json)

    #new_user = User()
    # retrieve user dimensions from db 
    # find size with same dimensions in db 
    # return the size id, name, size chart and retailer 
    # return error message if no match found 

    return {"message": "Placeholder"}, 200
