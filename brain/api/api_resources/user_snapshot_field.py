from bson import ObjectId
from bson.json_util import dumps

from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class SnapshotField(BaseResource):
    url = '/users/<int:user_id>/snapshots/<string:snapshot_id>/<string:field_name>'

    def get(self, user_id, snapshot_id, field_name):
        user_info = self.db_connection.snapshots.find({consts.USER_ID: user_id, '_id': ObjectId(snapshot_id)},
                                                      {field_name: 1})
        return dumps(user_info)
