# lib from py
from flask import session, render_template
from datetime import datetime, timezone

# my lib
from app.lib import token

def authen():
    # check for token in session
    if "token" not in session:
        return render_template("login.html")
    
    current = datetime.now(timezone.utc)
    status, payload = token.getDataFromSession()

    # check for exp
    if not status or "exp" not in payload or payload["exp"] <= int(current.timestamp()):
        session.clear()
        return render_template("login.html")