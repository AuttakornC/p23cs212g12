# my lib
from app.routes.page import main
from app.models.deck import Deck
from app.models.deck_card import DeckCard
from app.models.card import Card
from app.models.deck_tag import DeckTag
from app.models.tag import Tag

# Written by Auttakorn Camsoi
# edit deck page
@main.route("/edit/<deck_id:deck_id>")
def edit_deck(deck_id):
    return

# schema = {
#     "deck_id": str,
#     "name": str,
#     "cards": [
#         {
#             "id": int,
#             "question": str,
#             "answer": str
#             "player_id": int,
#             "form_dict": bool
#         } #...
#     ],
#     "tags": [
#         {
#             "id": int,
#             "name": str
#         }
#     ]
# }