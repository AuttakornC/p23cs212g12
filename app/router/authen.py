from app import app

@app.route("/api/authen")
def api_authen():
    return "API for authen."