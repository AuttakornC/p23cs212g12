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
    db.session.add(Player("auttakorn.camsoi@gmail.com", "Auttakorn Camsoi", "auttakorn1403"))
    db.session.add(Player("auttakorn1403@gmail.com", "AuttakornC14", "auttakorn1403"))
    db.session.commit()
    db.session.add(Deck("Auttakorn", False, 1))
    db.session.commit()
    db.session.add(Card("Ant", "มด", 2))
    db.session.add(Card("ant", "มด", None, True))
    db.session.add(Card("cat", "แมว", 1))
    db.session.add(Card("dog", "หมา", 1))
    db.session.add(Tag("animal"))
    db.session.add(Tag("auttakorn"))
    db.session.commit()
    db.session.add(DeckCard(1, 1))
    db.session.add(DeckCard(2, 1))
    db.session.add(DeckCard(3, 1))
    db.session.add(DeckCard(4, 1))
    db.session.add(DeckTag(1, 1))
    db.session.add(DeckTag(2, 1))
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