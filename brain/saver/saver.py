import furl
from pymongo import MongoClient

from brain.utils import build_queue_connection_from_url
from brain.utils import consts, saver_deserialize


class Saver:
    def __init__(self, database_url, queue_url=None):
        if furl.furl(database_url).scheme != 'mongodb':
            raise Exception('DB not Supported!')
        self.db = MongoClient(database_url)[consts.DB_NAME]
        if queue_url is not None:
            self.queue = build_queue_connection_from_url(queue_url)

    def save(self, topic, data):
        """
        save data in the db

        :param topic: topic of the data
        :param data: data to be saved
        :return:
        """
        user_id, datetime, save_data = saver_deserialize(data)

        if topic == consts.USER_TOPIC:
            self.db.users.update_one({consts.USER_ID: user_id}, {'$set': save_data}, upsert=True)

        self.db.snapshots.update_one({consts.USER_ID: user_id, consts.DATETIME: datetime},
                                     {'$set': {topic: save_data}}, upsert=True)

    def saver_callback(self):
        def on_message(ch, method, properties, body):
            topic = method.routing_key
            self.save(topic, body)

        return on_message

    def run(self):
        self.queue.exchange_declare(consts.PARSER_OUTPUT_EXCHANGE_NAME, 'topic')
        self.queue.anonymous_queue_declare_and_bind(consts.PARSER_OUTPUT_EXCHANGE_NAME, self.saver_callback(), '#')
        self.queue.start_consuming()
