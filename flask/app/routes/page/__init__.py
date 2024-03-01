from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")


# lib from py
from app.routes.page import home, explore, add, play, profile


