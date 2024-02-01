from app import app

@app.route("/<path:path>")
def notfound(path):
    return "Not found."