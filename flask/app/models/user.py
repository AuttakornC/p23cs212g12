from app import db
from sqlalchemy_serializer import SerializerMixin
from bcrypt import gensalt, hashpw

# Model of User
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    # use for check bruteforce
    failround = db.Column(db.Integer)

    def __init__(self, email:str, password:str):
        self.email = email
        self.password = hashpw(password.encode(), gensalt())
        self.failround = 0