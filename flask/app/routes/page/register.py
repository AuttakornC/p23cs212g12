from app import app

@app.route("/register")
def register():
    return "Register"