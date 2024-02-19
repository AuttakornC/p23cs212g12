# lib from py
from flask import jsonify

def badRequest(err):
    return jsonify({ "message" : "bad request.", "err": err }), 400

def success():
    return jsonify({ "message" : "success" }), 200

def successBody(data):
    return jsonify({ "message": "success", "data": data }), 200