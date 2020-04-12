from brain.utils import consts
from .client import Client


def upload_sample(file, host=consts.SERVER_DEFAULT_HOST, port=consts.SERVER_DEFAULT_PORT, test=False):
    """
    Upload snapshots to server

    :param test: configures the client for testing, false by default.
    :param host: ip of server
    :param port: port of server
    :param file: path to the file that contains the sample
    :return:
    """
    client = Client(host, port, file)
    client.upload()
