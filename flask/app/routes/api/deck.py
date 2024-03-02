# python lib
from flask import request

# my lib
from app.routes.api import api
from app.lib.token import getDataFromSession
from app.routes.api._deck.create import create_deck
from app.routes.api._deck.edit import updateDeck

@api.route("/deck", methods=["POST", "DELETE", "PATCH"])
def deck():
    user_data = getDataFromSession()
    if request.method == "POST":
        return create_deck(request.get_json(), user_data)
    if request.method == "PATCH":
        return updateDeck(request.get_json(), user_data)