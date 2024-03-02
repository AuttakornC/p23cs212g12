from app.lib.request import successBody
from app.models.deck import Deck
from app.models.player import Player
from app.models.deck_card import DeckCard

# write by Rachata
def get_my_deck(user_data):
    show = Deck.query.filter_by(player_id=user_data["id"])
    user = Player.query.get(user_data["id"])
    # print(user_data)
    json_show = []
    for i in show:
        temp = i.to_dict()
        temp["username"] = user.name
        temp["avatar_url"] = user.avatar_url
        deck_card = DeckCard.query.filter_by(deck_id=temp["id"])
        deck_card = len(list(map(lambda x: x.to_dict(), deck_card)))
        temp["len_card"] = deck_card
        json_show.append(temp)
        # print(i)
    # json_show = list(map(lambda x: x.to_dict(), show))
    
    print(json_show)
    return successBody(json_show)