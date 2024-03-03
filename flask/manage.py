# write by Mesanee Laihueang 650510676


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
    #     db.session.add(BlogEntry("เทสเตอร์","นี้คือเสียงจากเด็กคอม", "test@test.com"))
    db.session.add(Player(email='didi@gmail.com',
                   username='Didi', password='012345'))
    db.session.add(Player(email='dudu@gmail.com',
                   username='Dudu', password='012345'))
    db.session.commit()

    db.session.add(Deck(name='Animal', is_public=True, user_id=1))
    db.session.add(Deck(name='Color', is_public=True, user_id=2))
    # db.session.commit()

    db.session.commit()

    db.session.add(Card(question="ant", answer="มด", player_id=1))
    db.session.add(Card(question="cat", answer="แมว", player_id=1))
    db.session.add(Card(question="dog", answer="หมา", player_id=1))
    db.session.add(Card(question="buffalo", answer="ควาย", player_id=1))
    db.session.add(Card(question="red", answer="แดง", player_id=2))
    db.session.add(Card(question="pink", answer="ชมพู", player_id=2))
    db.session.add(Card(question="blue", answer="นํ้าเงิน", player_id=2))
    db.session.commit()

    # deck ที่ 1 มี card 4 id
    db.session.add(DeckCard(1, 1))
    db.session.add(DeckCard(2, 1))
    db.session.add(DeckCard(3, 1))
    db.session.add(DeckCard(4, 1))
    # db.session.commit()

    # db.session.commit()

    db.session.add(DeckCard(5, 2))
    db.session.add(DeckCard(6, 2))
    db.session.add(DeckCard(7, 2))
    db.session.commit()

    db.session.add(Tag('CS'))
    db.session.add(Tag('Eng'))
    db.session.commit()

    db.session.add(DeckTag(1,1))
    db.session.add(DeckTag(1,2))
    db.session.add(DeckTag(2,1))
    db.session.commit()

if __name__ == "__main__":
    cli()
