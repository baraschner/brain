from bson import ObjectId
import flask

from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class SnapshotFieldData(BaseResource):
    """
    Get the data of binary fields.
    """
    url = '/users/<int:user_id>/snapshots/<string:snapshot_id>/<string:field_name>/data'

    def get(self, user_id, snapshot_id, field_name):
        info = self.db_connection.snapshots.find_one({consts.USER_ID: user_id, '_id': ObjectId(snapshot_id)},
                                                     {field_name: 1, '_id': 0})

        with open(info[field_name]['path'], 'rb') as f:
            content = f.read()

        response = flask.make_response(content)
        response.headers['content-type'] = info[field_name]['content-type']
        return response
