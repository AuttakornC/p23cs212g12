# lib from py
from flask import render_template, jsonify

# my lib
from app.routes.page import main 
from app.models.player import Player
from app import app

@main.route("/play")
def play():
    return render_template("play.html", deck_detail={"name": "Hello"})
    # return "hello"


