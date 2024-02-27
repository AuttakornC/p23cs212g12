from flask import jsonify, render_template, redirect, url_for, flash, request, redirect
from app.routes.api import api
from app.models.deck import Deck
from app import app


@api.route("/explore/decks")
def explore_db_decks():
    decks = []
    db_decks = Deck.query.all()

    decks = list(map(lambda x: x.to_dict(), db_decks))
    app.logger.debug("DB decks: " + str(decks))

    return jsonify(decks)

# @main.route("/old_explore")
# def old_explore():
#     return render_template("old_explore.html")
