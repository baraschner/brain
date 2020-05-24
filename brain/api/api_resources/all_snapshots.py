from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class UserSnapshots(BaseResource):
    """
    Returns the id and timestamp of the available snapshots.
    """
    url = '/users/<int:user_id>/snapshots'

    def get(self, user_id):
        find_key = {consts.USER_ID: user_id}
        snapshots = self.db_connection.snapshots.find(find_key, {consts.DATETIME: 1})

        result = []

        for snapshot in snapshots:
            snapshot['id'] = str(snapshot['_id'])
            del snapshot['_id']
            result.append(snapshot)

        return result
