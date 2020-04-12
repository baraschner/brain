import fire
from brain.utils import consts
from .client import Client


def upload_cli(file, host=consts.SERVER_DEFAULT_HOST, port=consts.SERVER_DEFAULT_PORT):
    """

    :param host: ip of server
    :param port: port of server
    :param file: file in format mind.gz that contains the sample
    :return:
    """
    client = Client(host, port, file)
    client.upload()


if __name__ == '__main__':
    fire.Fire(upload_cli)
