from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

from brain.utils import flask_tools


def run(host, port, url):
    app = Flask(__name__)
    api = Api(app)
    db_connection = MongoClient(url)
    flask_tools.api_driver(api, __file__, db_connection)

    app.run(host=host, port=port)
