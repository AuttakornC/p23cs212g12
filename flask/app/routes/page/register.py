from app.routes.page import main
from flask import render_template

@main.route("/register")
def register():
    return render_template("register.html")