from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

from brain.utils import flask_tools


def run_api_server(host, port, database_url):
    """
    Runs the api server

    :param host: ip to bind
    :param port: port to bind
    :param database_url: url of database from which the api will get the data
    :return:
    """
    app = Flask(__name__)
    api = Api(app)
    db_connection = MongoClient(database_url)
    flask_tools.api_driver(api, __file__, db_connection) #automatically initializes api from api_resources

    app.run(host=host, port=port)

