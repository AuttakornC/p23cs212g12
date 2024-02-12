# lib from py
from flask import render_template

# my lib
from app.routes.page import main

@main.route("/login")
def login():
    return render_template("login.html")