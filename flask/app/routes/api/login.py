# lib from py
from bcrypt import checkpw
from datetime import datetime, timezone
from flask import request

# my lib
from app import app
from app.routes.api import api
from app.models.user import User
from app.lib.validate import emailValidate, lengthCheck, EMAIL_ERR, PASS_LEN, EMAIL_NOT_FOUND, BODY_NOT_CORRECT, PASS_WRONG
from app.lib.request import success, badRequest
from app.lib.token import encodeJWT

@api.route("/login", methods=["POST"])
def api_login():

    # check request body
    try:
        body = request.get_json()
        email, password = body["email"], body["password"]
    except Exception as err:
        app.logger.debug(str(err))
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
    if checkpw(str(password).encode(), user.password.encode()):
        payload = { "id": user.id, "email": user.email, "username": user.username, "exp": int(datetime.now(timezone.utc).timestamp()) }
        encodeJWT(payload)
        return success()

    return badRequest(PASS_WRONG)