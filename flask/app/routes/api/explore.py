from flask import jsonify, render_template, redirect, url_for, flash, request, redirect
from app.routes.api import api
from app.models.deck import Deck
from app import app
from app.models.player import Player
from app.models.deck_card import DeckCard
from app.models.card import Card
# python lib
from sqlalchemy import func
from app.lib.token import getDataFromSession
from app.lib.request import successBody


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
    cards = explore_db_cards()

    each_deck = []
    # ลูปแต่ละ deck
    for i in range(len(decks)):
        id_deck = decks[i]['id']
        dict_deck = {}
        card_in_deck = {}
        num_card = 0
        # ดูแต่ละคู่ของ deck และ card
        for j in decks_cards:
            # ดูว่าใน deck นี้มี card อะไรบ้างจาก decks_cards
            if j['deck_id'] == id_deck:
                num_card += 1
                for k in cards:
                    if k['id'] == j['card_id']:
                        question = k['question']
                        answer = k['answer']
                        card_in_deck['question'] = question
                        card_in_deck['answer'] = answer
        dict_deck['cards'] = card_in_deck
        dict_deck['num_card'] = num_card
        dict_deck['name'] = decks[i]['name']

        for j in players:
            if decks[i]['player_id'] == j['id']:
                dict_deck['player_name'] = j['name']
        each_deck.append(dict_deck)

    app.logger.debug("decks:", each_deck)
    return jsonify(each_deck)


# Written by Auttakorn Camsoi
# route for get a suggest
@api.route("/suggest")
def suggest():
    user_data = getDataFromSession()
    # print(user_data.id)
    word = request.args.get("search")

    result = {"owner": [], "other": []}

    # select our
    own_card = Card.query.filter(func.lower(Card.question) == func.lower(
        word), Card.player_id == user_data["id"], Card.is_deleted == False)
    result["owner"] = list(map(lambda x: x.to_dict(), own_card))

    # select other
    all_card = Card.query.filter(func.lower(Card.question) == func.lower(
        word), Card.player_id != user_data["id"], Card.is_deleted == False)
    all_card = list(map(lambda x: x.to_dict(), all_card))
    for card_info in all_card:
        deck_card = DeckCard.query.filter_by(card_id=card_info["id"])
        all_decks = list(map(lambda x: x.to_dict()["deck_id"], deck_card))
        for deck_id in all_decks:
            deck_info = Deck.query.get(deck_id)
            if deck_info.is_public:
                result["other"].append(card_info)
                break

    return successBody(result)
