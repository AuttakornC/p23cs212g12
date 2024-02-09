from app import app
from flask import session, redirect, render_template

@app.route("/")
def home():
    if "token" in session:
        return render_template("home.html")
    else:
        return redirect("/login")