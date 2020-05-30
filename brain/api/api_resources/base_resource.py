from flask_restful import Resource


class BaseResource(Resource):
    def __init__(self, db_connection):
        self.db_connection = db_connection
