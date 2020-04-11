import json
import logging
from flask import Flask, request
from flask_restful import Resource, Api
from bson import BSON

from brain.protocol import HelloResponse
from brain.utils import build_queue_connection_from_url
from brain.utils import consts
from brain.parsers import Parser


def run(host, port, url):
    app = Flask(__name__)
    logger = logging.getLogger()
    app.logger = logger
    api = Api(app)


    queue = build_queue_connection_from_url(url)
    queue.exchange_declare(consts.PARSER_INPUT_EXCHANGE_NAME, 'fanout')

    @api.resource('/config')
    class Hello(Resource):
        def get(self):
            hello_response = HelloResponse(Parser.get_supported_fields())
            return hello_response.to_json()

    @api.resource('/snapshot')
    class Snapshot(Resource):
        def post(self):
            data = BSON.decode(request.get_data())
            queue.publish(consts.PARSER_INPUT_EXCHANGE_NAME, json.dumps(data))

    app.run(host=host, port=port)
