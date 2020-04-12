import json
import logging
from flask import Flask, request
from flask_restful import Resource, Api
from bson import BSON

from brain.protocol import HelloResponse
from brain.utils import build_queue_connection_from_url
from brain.utils import consts
from brain.parsers import Parser


def run_server(host, port, queue_url, publish=None):
    """
    runs the server. the server can either publish to a queue or get a publish function

    :param host: ip to bind
    :param port: port to bind
    :param queue_url: url of message queue
    :param publish: public function, None if using queue
    :return:
    """
    app = Flask(__name__)
    logger = logging.getLogger()
    app.logger = logger
    api = Api(app)
    queue = None

    if queue_url is not None:
        queue = build_queue_connection_from_url(queue_url)
        queue.exchange_declare(consts.PARSER_INPUT_EXCHANGE_NAME, 'fanout')

    @api.resource('/config')
    class Config(Resource):
        """
        Config Messages in which the client gets the supported fields
        """
        def get(self):
            hello_response = HelloResponse(Parser.get_supported_fields())
            return hello_response.to_json()

    @api.resource('/snapshot')
    class Snapshot(Resource):
        """
        Snapshot Messages in which the client uploads the snapshot
        """
        def post(self):
            """
            Recieve Snapshot and either pass the result to queue or publish function
            """
            data = BSON.decode(request.get_data())
            if queue is not None:
                queue.publish(consts.PARSER_INPUT_EXCHANGE_NAME, json.dumps(data))
            else:
                publish(json.dumps(data))

    app.run(host=host, port=port)
