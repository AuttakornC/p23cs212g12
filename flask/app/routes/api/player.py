from flask import jsonify, render_template, redirect, url_for, flash, request, redirect
from app.routes.api import api
from app.models.player import Player
from app import app


@api.route("/explore/players")
def player_db_decks():
    players = []
    db_players = Player.query.all()

    players = list(map(lambda x: x.to_dict(), db_players))
    app.logger.debug("DB players: " + str(players))

    return jsonify(players)

# @main.route("/old_explore")
# def old_explore():
#     return render_template("old_explore.html")
