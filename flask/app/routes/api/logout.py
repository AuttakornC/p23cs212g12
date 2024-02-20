# lib from py
from flask import session, redirect, url_for

# my lib
from app.routes.api import api

@api.route("/logout")
def api_logout():
    session.clear()
    return redirect(url_for("main.home"))