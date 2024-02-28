from flask import jsonify, render_template, redirect, url_for, flash, request, redirect
from app.routes.api import api
from app.models.deck import Deck
from app import app
from app.models.player import Player
from app.models.deck_card import DeckCard
from app.models.card import Card


@api.route("/explore/decks")
def explore_db_decks():
    decks = []
    db_decks = Deck.query.all()

    decks = list(map(lambda x: x.to_dict(), db_decks))
    app.logger.debug("DB decks: " + str(decks))

    # return jsonify(decks)
    return decks


@api.route("/explore/players")
def explore_db_player():
    players = []
    db_players = Player.query.all()

    players = list(map(lambda x: x.to_dict(), db_players))
    # app.logger.debug("DB players: " + str(players))

    # return jsonify(players)
    return players


@api.route("/explore/decks/cards")
def explore_db_decks_cards():
    decks_cards = []
    db_decks_cards = DeckCard.query.all()
    # app.logger.debug("db_decks_cards:", db_decks_cards)
    decks_cards = list(map(lambda x: x.to_dict(), db_decks_cards))
    # app.logger.debug("DB decks_cards: " + str(decks_cards))

    # return jsonify(decks_cards)
    return decks_cards


@api.route("/explore/cards")
def explore_db_cards():
    cards = []
    db_cards = Card.query.all()
    # app.logger.debug("db_decks_cards:", db_decks_cards)
    cards = list(map(lambda x: x.to_dict(), db_cards))
    # app.logger.debug("DB cards: " + str(cards))

    # return jsonify(decks_cards)
    return cards


@api.route("/explore/all/decks")
def check_card_in_deck():

    decks = explore_db_decks()
    players = explore_db_player()
    decks_cards = explore_db_decks_cards()
    # cards = explore_db_cards()

    each_deck = []
    # ลูปแต่ละ deck
    for i in range(len(decks)):
        id_deck = decks[i]['id']
        dict_deck = {}
        num_card = 0
        # ดูแต่ละคู่ของ deck และ card
        for j in decks_cards:
            # ดูว่าใน deck นี้มี card อะไรบ้างจาก decks_cards
            if j['deck_id'] == id_deck:
                num_card += 1
        dict_deck['num_card'] = num_card
        dict_deck['name'] = decks[i]['name']

        for j in players:
            if decks[i]['player_id'] == j['id']:
                dict_deck['player_name'] = j['name']
        each_deck.append(dict_deck)
    return jsonify(each_deck)
