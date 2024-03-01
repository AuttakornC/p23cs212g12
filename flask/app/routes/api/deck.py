# python lib
from flask import request

# my lib
from app.routes.api import api
from app.lib.token import getDataFromSession
from app.routes.api._deck.create import create_deck

@api.route("/deck", methods=["POST", "DELETE", "PUT"])
def deck():
    user_data = getDataFromSession()
    if request.method == "POST":
        return create_deck(request.get_json(), user_data)