# lib from py
from flask.cli import FlaskGroup

# my lib
from app import app, db
from app.models.player import Player
from app.models.deck import Deck
from app.models.card import Card
from app.models.deck_tag import DeckTag
from app.models.tag import Tag
from app.models.deck_card import DeckCard

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    a = Player("auttakorn@camsoi.com", "Auttakorn Camsoi", "1234567890")
    b = Player("auttakorn@gmail.com", "Aut Cam", "1234567890")
    db.session.add(a)
    db.session.add(b)
    db.session.flush()
    db.session.commit()
    db.session.add(Tag("auttakorn"))
    db.session.add(Tag("aut"))
    db.session.add(Tag("food"))
    db.session.add(Tag("sci"))
    db.session.add(Deck("Test1", True, 1))
    db.session.add(Deck("Test2", False, 2))
    db.session.commit()
    db.session.add(Card("ANT", "มด", 1))
    db.session.commit()
    db.session.add(DeckCard(1, 1))
    db.session.add(DeckCard(1, 2))
    db.session.commit()

@cli.command("test_db")
def test_db():
    all_deck_card = DeckCard.query.filter_by(card_id=1)
    all_deck_data = Deck.query.filter(Deck.id.in_(list(map(lambda x: x.to_dict()["deck_id"], all_deck_card))), Deck.player_id == 1)
    # all_deck_data = Deck.query.filter(Deck.player_id == 1)
    print(len(list(map(lambda x: x.to_dict(),all_deck_card))))
    print(len(list(map(lambda x: x.to_dict(),all_deck_data))))

if __name__ == "__main__":
    cli()