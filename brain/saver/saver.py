import json

import furl
from pymongo import MongoClient

from brain.utils import build_queue_connection_from_url
from brain.utils import consts


class Saver:

    def get_db_info_from_url(self, db_url):
        url_obj = furl.furl(db_url)
        db_type = url_obj.scheme
        if db_type != 'mongodb':
            raise Exception('DB not Supported!')

    def __init__(self, database_url, queue_url=None):
        self.get_db_info_from_url(database_url)
        self.client = MongoClient(database_url)
        if queue_url is not None:
            self.queue = build_queue_connection_from_url(queue_url)

    def save(self, topic, data):
        db = self.client[consts.DB_NAME]
        json_data = json.loads(data)
        data = json_data[consts.DATA]

        if topic == consts.USER_TOPIC:
            user_id = data[consts.USER_ID]
            return db.users.update_one({consts.USER_ID: {'$eq': user_id}}, {'$set': data}, upsert=True)
        header = json_data[consts.HEADER]
        return db.snapshots.update_one(
            {consts.USER_ID: header[consts.USER_ID], consts.DATETIME: header[consts.DATETIME]}, {'$set': {topic: data}},
            upsert=True)

    def saver_callback(self):
        def on_message(ch, method, properties, body):
            topic = method.routing_key
            self.save(topic, body)

        return on_message

    def run(self):
        self.queue.exchange_declare(consts.PARSER_OUTPUT_EXCHANGE_NAME, 'topic')
        self.queue.anonymous_queue_declare_and_bind(consts.PARSER_OUTPUT_EXCHANGE_NAME, self.saver_callback(), '#')
        self.queue.start_consuming()
