from app import app
from flask import session, redirect
from app.routes.page.login import login

@app.route("/")
def home():
    if "token" in session:
        return "Home"
    else:
        return redirect("/login")