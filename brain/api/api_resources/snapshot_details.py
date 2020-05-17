from bson import ObjectId
from bson.json_util import dumps

from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class SnapshotDetails(BaseResource):
    url = '/users/<int:user_id>/snapshots/<string:snapshot_id>'

    def get(self, user_id, snapshot_id):
        snapshot = self.db_connection.snapshots.find_one({consts.USER_ID: user_id, '_id': ObjectId(snapshot_id)},{'_id':0}

        snapshot['_id'] = str(snapshot['_id'])
        return snapshot
