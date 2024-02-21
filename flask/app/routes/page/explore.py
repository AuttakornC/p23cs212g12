
from flask import render_template
from app.routes.page import main


@main.route("/explore")
def explore():
    return render_template("explore.html")
