from flask import Flask

app = Flask(__name__, static_folder="client/static")
app.url_map.strict_slashes = False
app.config["DEBUG"] = True

# serve client
from app import client

# api server
from app.server import api
app.register_blueprint(api, url_prefix="/api") # create route prefix to api path