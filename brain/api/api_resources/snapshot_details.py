from bson import ObjectId

from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class SnapshotDetails(BaseResource):
    """

    Returns information about the available fields in a user's snapshot.

    """
    url = '/users/<int:user_id>/snapshots/<string:snapshot_id>'

    def get(self, user_id, snapshot_id):
        snapshot = self.db_connection.snapshots.find_one({consts.USER_ID: user_id, '_id': ObjectId(snapshot_id)})

        snapshot.pop('_id')
        snapshot.pop('userId')
        datetime = snapshot.pop('datetime')

        return {'_id': snapshot_id, 'datetime': datetime, 'available fields': list(snapshot.keys())}
