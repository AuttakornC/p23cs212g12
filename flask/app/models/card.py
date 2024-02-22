# lib from py
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

# my lib
from app import db

class Card(db.Model, SerializerMixin):
    __tablename__ = "cards"
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    answer = db.Column(db.String())
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    is_deleted = db.Column(db.Boolean, default=False)
    delete_at = db.Column(db.DateTime)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.is_deleted = False
        self.delete_at = None
    
    def update(self, question, answer):
        self.question = question
        self.answer = answer
    
    def delete(self):
        self.is_deleted = True
        self.delete_at = datetime.now(timezone.utc)
