from app import app
from flask import jsonify

@app.route("/")
def home():
    return "auttakorn say : Hello world!"


@app.route("/phonebook")
def index():
    return app.send_static_file("phonebook.html")

@app.route("/api/data")
def data():
    # define some data
    d = {
        "Alice": "(708) 727-2377",
        "Bob": "(305) 734-0429"
    }
    return jsonify(d)
