from app import app, oauth, db
from app.routes.api import api
from flask import url_for, session, redirect
from app.models.user import User
from datetime import datetime, timezone
from jwt import encode

@api.route("/login/google")
def login_google():

    oauth.register(
        "google",
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # url to redirect to
    redirect_url = url_for("api.login_google_auth", _external=True)
    return oauth.google.authorize_redirect(redirect_url)

@api.route("/login/google/auth")
def login_google_auth():
    token = oauth.google.authorize_access_token()

    user_info = token['userinfo']
    app.logger.debug(user_info)
    user = User.query.filter_by(email=user_info["email"]).first()
    if not user:
        name = user_info.get('given_name','') + " " + user_info.get('family_name','')
        new_user = User(user_info["email"], name, "-")
        new_user.updatePass("-", False)
        new_user.updateAVT(user_info["picture"])
        db.session.add(new_user)
        db.session.commit()

    user = User.query.filter_by(email=user_info["email"]).first()
    payload = { "id": user.id, "email": user.email, "exp":  int(datetime.now(timezone.utc).timestamp())}
    encoded = encode(payload, app.config["SECRET_KEY"])
    session["token"] = encoded
    return redirect(url_for("main.home"))
    