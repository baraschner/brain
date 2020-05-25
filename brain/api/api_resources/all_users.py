from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class AllUsers(BaseResource):
    """
    Returns all users.
    """
    url = '/users'

    def get(self):
        return list(self.db_connection.users.find({}, {'username': 1, consts.USER_ID: 1, '_id': 0}))
