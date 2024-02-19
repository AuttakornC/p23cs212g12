# lib from py
from flask import session

# my lib
from app.routes.api import api

@api.route("/logout")
def api_logout():
    session.clear()
    return ""