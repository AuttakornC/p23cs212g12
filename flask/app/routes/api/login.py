from app.routes.api import api
from flask import request, jsonify, current_app
from app.models.user import User
from bcrypt import checkpw
from jwt import encode

@api.route("/login")
def login():
    body = request.data
    email, password = "", ""
    # check for input wrong
    try:
        email, password = body["email"], body["password"]
    except:
        return jsonify({ "message": "bad request.", "code": "REQ_WRONG" })
    
    user = User.query.filter_by(email=email).first()

    # don't found user
    if not user:
        return jsonify({ "message": "email not found.", "code": "EMAIL_NOT_FOULD" }), 400
    
    # check password in database
    if checkpw(str(password).encode(), user.password):
        secret = current_app.config['SECRET_KEY']               # get secret key at app/__init__.py
        payload = { "id": user.id, "email": user.email }
        encoded = encode(payload, secret)                       # use jwt encode to get token
        return jsonify({ "message": "authen success.", "code": "AUTHEN_SUC", "token":  encoded})

    return jsonify({ "message": "password wrong", "code": "PSW" })