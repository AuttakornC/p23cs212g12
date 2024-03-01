
from flask import render_template, jsonify
from app.routes.page import main
from app.models.player import Player
from app import app


# lib from py
from flask import render_template

# my lib
from app.routes.page import main


@main.route("/play")
def play():
    return render_template("play.html", deck_detail={"name": "Hello"})
    # return "hello"
