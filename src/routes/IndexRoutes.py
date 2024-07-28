from flask import Blueprint, jsonify
from decouple import config
import traceback

main = Blueprint('index_blueprint', __name__)


@main.route("/")
def index():
    return jsonify({'message':'Hello world from Flask and Blueprint '+config('APP_MESSAGE')})
