from bson import ObjectId

from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class SnapshotField(BaseResource):
    """
    Returns the value of a field in a specific snapshot.
    """

    url = '/users/<int:user_id>/snapshots/<string:snapshot_id>/<string:field_name>'

    def get(self, user_id, snapshot_id, field_name):
        field_info = self.db_connection.snapshots.find_one({consts.USER_ID: user_id, '_id': ObjectId(snapshot_id)},
                                                           {field_name: 1, '_id': 0})
        return field_info[field_name]
