from flask import session, render_template
# lib from py
from jwt import decode, encode

# my lib
from app import app

def getDataFromSession():
    '''Function for get data from current session'''
    try:
        token = session["token"]
        data = decode(token, app.config["SECRET_KEY"])
        return True, data
    except:
        return False, render_template("login.html")

def encodeJWT(data):
    '''Function for encode data to token and set to session["token"]'''
    session["token"] = encode(data, app.config["SECRET_KEY"])