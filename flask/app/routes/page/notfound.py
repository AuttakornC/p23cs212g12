from app import app
from flask import render_template

@app.route("/<path:path>")
def not_found(path):
    return render_template('notfound.html')