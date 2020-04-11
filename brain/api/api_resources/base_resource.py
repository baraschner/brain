from flask_restful import Resource

from brain.utils import consts


class BaseResource(Resource):
    def __init__(self, db_connection):
        self.db_connection = db_connection[consts.DB_NAME]
