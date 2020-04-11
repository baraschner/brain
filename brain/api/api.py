from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

from brain.utils import flask_tools


def run_api_server(host, port, database_url):
    app = Flask(__name__)
    api = Api(app)
    db_connection = MongoClient(database_url)
    flask_tools.api_driver(api, __file__, db_connection)

    app.run(host=host, port=port)

