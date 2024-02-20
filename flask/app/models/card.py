# lib from py
from sqlalchemy_serializer import SerializerMixin

# my lib
from app import db

class Card(db.Model, SerializerMixin):
    __tablename__ = "cards"
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    answer = db.Column(db.String())
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, question, answer, deck_id):
        self.question = question
        self.answer = answer
        self.deck_id = deck_id
        self.deleted = False
    
    def update(self, question, answer):
        self.question = question
        self.answer = answer
    
    def delete(self):
        self.deleted = True