from pathlib import Path

import requests
from bson import BSON

from brain.client.readers import ProtobufReader


def _check_file(file):
    path = Path(file)
    if len(path.suffixes) != 2:
        return False
    return path.suffixes[0] == '.mind' and path.suffixes[1] == '.gz'


class Client:
    def __init__(self, host, port, file):
        if not _check_file(file):
            raise Exception("File Type Not Supported")
        self.reader = ProtobufReader(file)

        self.address = f'{host}:{port}'

    def __send_message(self, url, message=None, method='GET'):
        """
        Send a message to a server

        :param url: url of server
        :param message: message to send, in case using post
        :param method: http method, default is get
        """
        url = f'http://{self.address}{url}'

        if method == 'GET':

            http_response = requests.get(url)
        else:

            http_response = requests.post(url, data=message)

        if http_response.status_code != 200:
            raise ValueError("Protocol Error")
        else:
            return http_response

    def _send_snapshot(self, user, snapshot):
        """
        upload a single snapshot to the server

        :param user: a dictionary that contains the user information
        :param snapshot: a dictionary that contains the snapshot to upload
        """
        snapshot_bson = BSON.encode({**user, **snapshot})
        self.__send_message('/snapshot', snapshot_bson, 'POST')

    def upload(self):
        """
        Upload the entire sample file to the server
        """
        hello_response = self.__send_message('/config').json()

        self.reader.set_supported_fields(hello_response['supported_fields'])
        user_dict = self.reader.read_user()

        for snapshot in self.reader:
            self._send_snapshot(user_dict, snapshot)
