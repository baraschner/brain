from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts


class UserInfo(BaseResource):
    """
    Returns details about the a user.
    """

    url = '/users/<int:user_id>'

    def get(self, user_id):
        user_info = self.db_connection.users.find_one({consts.USER_ID: user_id}, {'_id': 0})
        return user_info
