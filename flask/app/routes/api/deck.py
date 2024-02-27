# python lib
from flask import request

# my lib
from app.routes.api import api
from app.lib.token import getDataFromSession
from app.routes.api.deck_method.create import create_deck
from app.routes.api.deck_method.get import get_my_deck

@api.route("/deck", methods=["GET","POST", "DELETE", "PUT"])
def deck():
    user_data = getDataFromSession()
    if request.method == "POST":
        return create_deck(request.get_json(), user_data)
    return get_my_deck(user_data)