from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from pymongo import MongoClient

from brain.utils import flask_tools,consts


def run_api_server(host, port, database_url,test_db=None):
    """
    Runs the api server

    :param host: ip to bind
    :param port: port to bind
    :param database_url: url of database from which the api will get the data
    :return:
    """
    app = Flask(__name__)
    if test_db is not None:
        db = test_db
    else:
        db = MongoClient(database_url)[consts.DB_NAME]

    # automatically initializes api from api_resources
    flask_tools.api_driver(Api(app), __file__, (db,))

    CORS(app)

    app.run(host=host, port=port)
