# lib from py
from flask import render_template

# my lib
from app.routes.page import main 
from app.lib.token import getDataFromSession
from app.models.player import Player

@main.route("/")
def home():
    status, payload = getDataFromSession()
    if status:
        # print(payload["id"])
        player_data = Player.query.get(payload["id"])
        # print(player_data)
        return render_template("home.html", player_data=player_data.to_dict())
    else:
        return player_data