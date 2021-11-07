from flask import Blueprint, jsonify
from ...exception.exceptions import *
import json
errors = Blueprint('errors', __name__)

DEFAULT_CODE = 500
DEFAULT_MESSAGE = "Intern error"


@errors.app_errorhandler(Exception)
def handle_error(error):
    print(error)
    dto = {'code':DEFAULT_CODE, 'message': DEFAULT_MESSAGE}
    return jsonify(dto), 500

@errors.app_errorhandler(DatabaseIntegrationError)
def handle_error(error):
    print(error)
    dto = {'code':error.status_code, 'message': error.message}
    return jsonify(dto), 500

@errors.app_errorhandler(NotFoundException)
def handle_error(error):
    print(error)
    dto = {'code':error.status_code, 'message': error.message}
    return jsonify(dto), 404

def init_app(app):
    app.register_blueprint(errors)