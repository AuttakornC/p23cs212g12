from app.routes.api import api
from flask import request, jsonify, current_app
from app.models.user import User
from bcrypt import checkpw
from jwt import encode
from app.lib.validate import emailValidate, lengthCheck, EMAIL_ERR, PASS_LEN, EMAIL_NOT_FOUND, BODY_NOT_CORRECT, PASS_WRONG
from app.lib.request import successBody, badRequest

@api.route("/login")
def login():

    # check request body
    body = request.data
    email, password = "", ""
    try:
        email, password = body["email"], body["password"]
    except:
        return badRequest([BODY_NOT_CORRECT])
    
    # validate form
    fail_form = []
    if not emailValidate(email):
        fail_form.append(EMAIL_ERR)
    if not lengthCheck(password):
        fail_form.append(PASS_LEN)
    if len(fail_form) != 0:
        return badRequest(fail_form)

    user = User.query.filter_by(email=email).first()

    # don't found user
    if not user:
        return badRequest([EMAIL_NOT_FOUND])
    
    # check password in database
    if checkpw(str(password).encode(), user.password):
        secret = current_app.config['SECRET_KEY']               # get secret key at app/__init__.py
        payload = { "id": user.id, "email": user.email }
        encoded = encode(payload, secret)                       # use jwt encode to get token
        return successBody({ "token": encode })

    return badRequest(PASS_WRONG)