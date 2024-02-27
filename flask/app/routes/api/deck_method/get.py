from app.lib.request import successBody
from app.models.deck import Deck
# write by Rachata
def get_my_deck(user_data):
    show = Deck.query.filter_by(player_id=user_data["id"])
    json_show = list(map(lambda x: x.to_dict(), show))
    print(json_show)
    return successBody(json_show)