from app.routes.page import main
from flask import render_template

@main.route("/login")
def login():
    return render_template("login.html")