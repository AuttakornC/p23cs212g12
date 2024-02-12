# lib from py
from flask import render_template

# my lib
from app.routes.page import main 

@main.route("/")
def home():
    return render_template("home.html")