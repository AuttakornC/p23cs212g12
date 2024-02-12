# lib from py
from flask import render_template

# my lib
from app.routes.page import main

@main.route("/register")
def register():
    return render_template("register.html")