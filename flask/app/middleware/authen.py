from app import app
from flask import session, render_template
from jwt import decode

def authen():
    if "token" not in session:
        return render_template("login.html")