# lib from py
from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")

from app.routes.api import register, login, logout, google_login, fb_login, explore, player