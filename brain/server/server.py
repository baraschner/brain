import json
import logging
from datetime import datetime

from bson import BSON
from flask import Flask, request
from flask_restful import Resource, Api

from brain.parsers import get_supported_fields
from brain.utils import build_queue_connection_from_url
from brain.utils import consts, Context
from brain.utils.dumper import dump_binary_data


def run_server(host=consts.SERVER_DEFAULT_HOST, port=consts.SERVER_DEFAULT_PORT,
               queue_url=None, publish=None, base_save_path=consts.SAVE_PATH, test=False):
    """
    runs the server. the server can either publish to a queue or get a publish function

    :param test: testing configuration in which the app is returned and not run.
    :param host: ip to bind
    :param port: port to bind
    :param queue_url: url of message queue
    :param publish: public function, None if using queue
    :param base_save_path: base path to dump binary data

    :return:
    """
    app = Flask(__name__)
    logger = logging.getLogger()
    app.logger = logger
    api = Api(app)
    supported_fields = get_supported_fields()

    if queue_url is not None:
        queue = build_queue_connection_from_url(queue_url)
        queue.exchange_declare(consts.PARSER_INPUT_EXCHANGE_NAME, 'fanout')
    else:
        queue = None

    @api.resource('/config')
    class Config(Resource):
        """
        Config Messages in which the client gets the supported fields
        """

        def get(self):
            return {consts.SUPPORTED_FIELDS: supported_fields}

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
            user_id = data[consts.USER_ID]
            date = datetime.fromtimestamp(int(data[consts.DATETIME]) / 1000)
            context = Context(base_save_path, user_id, date)

            dump_binary_data(data, context)

            if queue is not None:
                queue.publish(consts.PARSER_INPUT_EXCHANGE_NAME, json.dumps(data))
            else:
                publish(json.dumps(data))

    if (test):
        return app
    app.run(host=host, port=port)
