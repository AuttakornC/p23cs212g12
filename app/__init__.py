from flask import Flask

app = Flask(__name__, static_folder="static", template_folder="template")
app.url_map.strict_slashes = False
app.config["DEBUG"] = True

# serve client
from app import router