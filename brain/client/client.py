import requests
from bson import BSON

from brain.client.readers import ProtobufReader


class Client:
    def __init__(self, host, port, file, test=None):
        self.file = file
        self.address = f'{host}:{port}'
        self.test = test

    def __send_message(self, url, message=None, method='GET'):
        """
        Send a message to a server

        :param url: url of server
        :param message: message to send, in case using post
        :param method: http method, default is get
        """
        url = f'http://{self.address}{url}'

        if method == 'GET':

            if self.test is not None:  # Client is being used as testing client
                return self.test.get(url)

            http_response = requests.get(url)
        else:
            if self.test is not None:  # Client is being used as testing client
                return self.test.post(url, data=message)

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
        reader = ProtobufReader(self.file)
        hello_response = self.__send_message('/config').json()

        reader.set_supported_fields(hello_response['supported_fields'])
        user_dict = reader.read_user()

        for snapshot in reader:
            self._send_snapshot(user_dict, snapshot)
            if self.test is not None:  # in testing, send just a single snapshot
                break
