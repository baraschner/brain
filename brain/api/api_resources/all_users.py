from brain.api.api_resources.base_resource import BaseResource
from brain.utils import consts
from bson.json_util import dumps


class AllUsers(BaseResource):
    url = '/users'

    def get(self):
        all_users = self.db_connection.users.find({},
                                                  {'username': 1, consts.USER_ID: 1, '_id': 0})
        return dumps(all_users)
