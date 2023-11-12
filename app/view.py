from app import app

@app.route("/")
def home():
    return "auttakorn say : Hello world!"


@app.route("/phonebook")
def index():
    return app.send_static_file("phonebook.html")
