from app.routes.api import api
from flask import session

@api.route("/logout")
def api_logout():
    session.clear()
    return ""