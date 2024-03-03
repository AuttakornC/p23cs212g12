# python lib
from flask import request

# my lib
from app.routes.api import api
from app.lib.token import getDataFromSession
from app.routes.api.deck_method.create import create_deck
from app.routes.api.deck_method.get import get_my_deck
from app.routes.api.deck_method.edit import updateDeck
from app.routes.api.deck_method.delete import delete_deck

@api.route("/deck", methods=["GET","POST", "DELETE", "PATCH"])
def deck():
    user_data = getDataFromSession()
    if request.method == "POST":
        return create_deck(request.get_json(), user_data)
    if request.method == "PATCH":
        return updateDeck(request.get_json(), user_data)
    if request.method == "DELETE":
        return delete_deck(request.args.get("id"), user_data)
    return get_my_deck(user_data)
''' schema [
    {'create_at': '2024-03-02 19:19:26', 'id': 3, 'delete_at': None, 
    'name': '', 'is_deleted': False, 'is_public': False, 'player_id': 3, 
    'username': 'รชต ธนัญชัย', 'avatar_url': 'https://lh3.googleusercontent.com/a/ACg8ocLU8_khO9j6dlSlrg7TyFRA3O1ECRnBxyXliCkNm4Lmbas=s96-c',
    'len_card': 1}, 
    {'create_at': '2024-03-02 19:19:51', 'id': 4, 'delete_at': None,
    'name': 't', 'is_deleted': False, 'is_public': True, 'player_id': 3,
    'username': 'รชต ธนัญชัย', 'avatar_url': 'https://lh3.googleusercontent.com/a/ACg8ocLU8_khO9j6dlSlrg7TyFRA3O1ECRnBxyXliCkNm4Lmbas=s96-c',
    'len_card': 0}]
'''

@api.route("/deck/delete", methods=["POST"])
def delete_decks():
    user_data = getDataFromSession()
    if request.method == "POST":
        return delete_deck(request.get_json(), user_data)
