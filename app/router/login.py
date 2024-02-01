from app import app

@app.route("/login")
def login_page():
    return "This is Login Page."