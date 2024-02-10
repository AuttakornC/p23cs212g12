from app import db
from sqlalchemy_serializer import SerializerMixin
from bcrypt import gensalt, hashpw

# Model of User
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    avatar_url = db.Column(db.String(255))
    # use for check bruteforce
    failround = db.Column(db.Integer)

    def __init__(self, email:str, username:str, password:str):
        self.email = email
        self.username = username;
        self.password = hashpw(password.encode(), gensalt()).decode()
        self.avatar_url = f'https://ui-avatars.com/api/?name={email[0]}+{email[1]}&background=f6d394&color=725c3a'
        self.failround = 0
    
    def updateAVT(self, avatar_url):
        self.avatar_url = avatar_url
    
    def updateName(self, name:str):
        self.name = name;