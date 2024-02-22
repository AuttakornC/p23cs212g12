# lib from py
from flask.cli import FlaskGroup

# my lib
from app import app, db
from app.models.player import Player
from app.models.deck import Deck
from app.models.card import Card
from app.models.deck_tag import DeckTag
from app.models.tag import Tag

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# @cli.command("seed_db")
# def seed_db():
#     db.session.add(BlogEntry("เทสเตอร์","นี้คือเสียงจากเด็กคอม", "test@test.com"))
#     db.session.commit()

if __name__ == "__main__":
    cli()