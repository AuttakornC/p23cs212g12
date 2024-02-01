from app import app

@app.route("/play")
def play():
    return "This is Play page."