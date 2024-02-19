# lib from py
from flask.cli import FlaskGroup

# my lib
from app import app, db
from app.models.user import User
from app.models.deck import Deck
from app.models.card import Card

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