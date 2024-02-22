# lib from py
from sqlalchemy_serializer import SerializerMixin

# my lib
from app import db

class Tag(db.Model, SerializerMixin):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, name):
        self.name = name
        self.deleted = False
    
    def update(self, name):
        self.name = name
    
    def delete(self):
        self.deleted = True