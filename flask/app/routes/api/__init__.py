from flask import Blueprint
api = Blueprint("api", __name__, url_prefix="/api")
# lib from py
from app.routes.api import deck, \
    tag, \
    suggest, \
    profile,\
    explore



