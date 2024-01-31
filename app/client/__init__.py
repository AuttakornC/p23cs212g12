from app import app

# client serve
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>") # anypath that is not in server side will redirect to index.html only
def serve(path):
    # serve index.html only
    return app.send_static_file("index.html")