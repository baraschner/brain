import json
from bson import BSON
import requests
from google.protobuf.json_format import MessageToDict
from brain.client.parsers import ProtobufParser

from brain.utils import User
from brain.utils import consts


class Client:
    def __init__(self, host,port, file):
        self.file = file
        self.address = f'{host}:{port}'

    def __send_message(self, url, message=None, method='GET'):
        """
        Send a message to a server

        :param url: url of server
        :param message: message to send, in case using post
        :param method: http method, default is get
        :return:
        """
        url = f'http://{self.address}/{url}'

        if method == 'GET':
            http_response = requests.get(url)
        else:
            http_response = requests.post(url, data=message)

        if http_response.status_code != 200:
            raise ValueError("Protocol Error")
        else:
            return http_response

    def upload(self):
        """
        Upload the snapshot file to the server
        :return:
        """
        parser = ProtobufParser(self.file)
        hello_response = json.loads(self.__send_message('config').json())
        user = parser.read_object(User())
        user_dict = MessageToDict(user, including_default_value_fields=True)
        user_dict[consts.USER_ID] = int(user_dict[consts.USER_ID]) # this is since protobuf doesn't preserver int64

        supported_fields = hello_response['supported_fields']
        for snapshot in parser:
            snapshot_dict = MessageToDict(snapshot, including_default_value_fields=True)
            # filtered = filter_json(snapshot_dict, supported_fields)
            filtered = snapshot_dict
            snapshot_bson = BSON.encode({**user_dict, **filtered})
            self.__send_message('snapshot',snapshot_bson , 'POST')
