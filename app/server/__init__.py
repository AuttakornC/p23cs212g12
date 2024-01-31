from flask import Blueprint

# use blueprint instead of app
api = Blueprint("api", __name__)

# EXAMPLE
# @api.route("path")
# def function_name():
#     return bra bra bra