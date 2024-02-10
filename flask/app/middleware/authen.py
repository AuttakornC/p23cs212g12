from flask import session, render_template

def authen():
    if "token" not in session:
        return render_template("login.html")
    # pass