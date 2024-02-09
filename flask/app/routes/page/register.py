from app import app
from flask import render_template

@app.route("/register")
def register():
    return render_template("register.html")