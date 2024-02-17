# lib from py
from sqlalchemy_serializer import SerializerMixin

# my lib
from app import db

class Deck(db.Model, SerializerMixin):
    __tablename__ = "decks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    public = db.Column(db.Boolean, default=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, name, type, user_id):
        self.name = name
        self.type = type
        self.user_id = user_id
    
    def update(self, name, type):
        self.name = name
        self.type = type