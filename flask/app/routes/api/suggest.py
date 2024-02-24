# python lib
from flask import request
from sqlalchemy import func

# my lib
from app.routes.api import api
from app.models.card import Card
from app.models.deck import Deck
from app.models.deck_card import DeckCard
from app.lib.token import getDataFromSession
from app.lib.request import successBody

@api.route("/suggest")
def suggest():
    user_data = getDataFromSession()
    # print(user_data.id)
    word = request.args.get("search")

    result = {"owner": [], "other": []}

    # select our
    own_card = Card.query.filter(func.lower(Card.question) == func.lower(word), Card.player_id == user_data["id"], Card.is_deleted == False)
    result["owner"] = list(map(lambda x: x.to_dict(), own_card))

    # select other
    all_card = Card.query.filter(func.lower(Card.question) == func.lower(word), Card.player_id != user_data["id"], Card.is_deleted == False)
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