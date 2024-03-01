# write by Mesanee Laihueang 650510676


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
from app.models.tag import Tag
from app.models.deck_tag import DeckTag


@api.route("/explore/decks")
def explore_db_decks():
    decks = []
    db_decks = Deck.query.all()

    decks = list(map(lambda x: x.to_dict(), db_decks))
    app.logger.debug("DB decks: " + str(decks))

    return jsonify(decks)
    # return decks
    
    
@api.route("/explore/tags")
def explore_db_tags():
    tags = []
    db_tags = Tag.query.all()
    tags = list(map(lambda x: x.to_dict(), db_tags))
    # app.logger.debug("DB cards: " + str(cards))

    return jsonify(decks_cards)
    # return tags


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





@api.route("/explore/decks/tags")
def explore_db_decks_tags():
    decks_tags = []
    db_decks_tags = DeckTag.query.all()
    # app.logger.debug("db_decks_cards:", db_decks_cards)
    decks_tags = list(map(lambda x: x.to_dict(), db_decks_tags))
    # app.logger.debug("DB decks_cards: " + str(decks_cards))

    # return jsonify(decks_cards)
    return decks_tags


@api.route("/explore/all/decks")
def check_card_in_deck():

    decks = []
    db_decks = Deck.query.all()
    decks = list(map(lambda x: x.to_dict(), db_decks))
    tags = []
    db_tags = Tag.query.all()
    tags = list(map(lambda x: x.to_dict(), db_tags))
    
    players = explore_db_player()
    decks_cards = explore_db_decks_cards()
    cards = explore_db_cards()
    decks_tags = explore_db_decks_tags()

    each_deck = []
    # ลูปแต่ละ deck
    for i in range(len(decks)):
        id_deck = decks[i]['id']
        dict_deck = {}
        card_in_deck = {}
        tag_in_deck = {}
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
                        card_in_deck[question] = answer
                        # card_in_deck['answer'] = answer
        
        dict_deck['cards'] = card_in_deck
        dict_deck['num_card'] = num_card
        dict_deck['name'] = decks[i]['name']

        for j in players:
            if decks[i]['player_id'] == j['id']:
                dict_deck['player_name'] = j['name']
                dict_deck['avatar_url'] = j['avatar_url']
                
        index = 0
        # ดูแต่ละคู่ของ deck และ tag
        for j in decks_tags:
            
            # ดูว่าใน deck นี้มี tag อะไรบ้างจาก decks_tags
            if j['deck_id'] == id_deck:
                for k in tags:
                    if k['id'] == j['tag_id']:
                        tag_in_deck[index] = k['name']
                        index+=1
                        # card_in_deck['answer'] = answer
                        
        dict_deck['tags'] = tag_in_deck       

        each_deck.append(dict_deck)

    # app.logger.debug("decks:", each_deck)
    return jsonify(each_deck)
