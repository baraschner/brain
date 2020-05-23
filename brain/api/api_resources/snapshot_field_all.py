from bson import ObjectId

from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class SnapshotFieldAll(BaseResource):
    """
        Returns all the info of a specific field in all snapshots of of a specific user.
    """
    url = '/users/<int:user_id>/all/<string:field_name>'

    def get(self, user_id, field_name):
        field_info = self.db_connection.snapshots.find({consts.USER_ID: user_id},
                                                       {field_name: 1, '_id': 0, consts.DATETIME:1})
        return list(field_info).sort(key = lambda x: x[consts.DATETIME])
