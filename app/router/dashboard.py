from app import app

@app.route("/")
@app.route("/dashboard")
@app.route("/home")
def home():
    return "This is Home."