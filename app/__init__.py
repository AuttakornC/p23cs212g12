from flask import Flask

app = Flask(__name__, static_folder="client/static")
app.url_map.strict_slashes = False
app.config["DEBUG"] = True