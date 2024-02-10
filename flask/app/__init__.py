import os
from flask import Flask
from werkzeug.debug import DebuggedApplication
from flask_sqlalchemy import SQLAlchemy
from app.middleware.authen import authen

app = Flask(__name__, static_folder='static', template_folder='template')
app.url_map.strict_slashes = False

app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = \
    'ce9262b39d8efd3757681a63ea7a6f97e4da7bcc10871a17'
app.config['JSON_AS_ASCII'] = False


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


# from app import route  # noqa
from app.routes.page import notfound
from app.routes.page import main
from app.routes.api import api
app.before_request_funcs = {
    "main": [authen],
    "api": []
}
app.register_blueprint(main)
app.register_blueprint(api)