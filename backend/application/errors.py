from application.classes.exception import CustomExceptionJson
from flask import jsonify

def handle_resource_not_found(e):
    res = CustomExceptionJson(str(e)).json()
    return jsonify(res), 404

def handle_bad_request(e):
    res = CustomExceptionJson(str(e)).json()
    return jsonify(res), 400

def handle_unhandled_exception(e: Exception):
    res = CustomExceptionJson(str(e)).json()
    return jsonify(res), 500