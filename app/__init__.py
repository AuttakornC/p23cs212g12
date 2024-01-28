from os import urandom
from flask import Flask


app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False

app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "ce9262b39d8efd3757681a63ea7a6f97e4da7bcc10871a17"
# SECRET_KEY = urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
app.config['JSON_AS_ASCII'] = False

from app import views # noqa