from bson.json_util import dumps
from api.api_resources.base_resource import BaseResource
from brain.utils import consts


class UserSnapshots(BaseResource):
    url = '/users/<int:user_id>/snapshots'

    def get(self, user_id):
        find_key = {consts.USER_ID: user_id}
        snapshots = self.db_connection.snapshots.find(find_key, {consts.DATETIME: 1})
        return dumps(snapshots)
