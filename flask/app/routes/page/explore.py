
from flask import render_template, jsonify
from app.routes.page import main
from app.models.deck import Deck
from app import app


@main.route("/explore",  methods=('GET', 'POST'))
def explore():
    return render_template("explore.html")


@main.route("/explore/decks")
def explore_db_decks():
    decks = []
    db_decks = Deck.query.all()

    decks = list(map(lambda x: x.to_dict(), db_decks))
    app.logger.debug("DB decks: " + str(decks))

    return jsonify(decks)

# @main.route("/old_explore")
# def old_explore():
#     return render_template("old_explore.html")