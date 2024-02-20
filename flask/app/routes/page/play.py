# lib from py
from flask import render_template

# my lib
from app.routes.page import main 

@main.route("/play")
def play():
    return render_template("play.html")
    # return "hello"