from app.routes.api import api
from flask import request, jsonify
from app.models.user import User
from app import db

def checkEmail(email:str):
    return len(email.split("@")) == 2 and email.split("@")[1].count(".")>0

@api.route("/register", methods=["POST"])
def register():
    body = request.data
    email, password, c_password = "", "", ""
    try:
        email, password, c_password = body["email"], body["password"], body["c_password"]
        if not checkEmail(email):
            raise "wrong format email."
    except:
        return jsonify({ "message": "bad request." }), 400
    
    if password == c_password:
        db.session.add(User(email, password))
        db.session.commit()
        return jsonify({ "message": "success" }), 200
    return jsonify({ "message": "password and confirm password not equal." }), 400