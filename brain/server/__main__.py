import fire

from .server import run_server
from brain.utils import consts


def run_server_cli(host=consts.LOCALHOST, port=consts.SERVER_DEFAULT_PORT, queue=consts.RABBIT_DEFAULT_URL):
    """
    runs the server on a given host and port with the message queue provided.
    :param host: ip address of host
    :param port: port to bind the server
    :param queue: url to connect to message queue
    :return:
    """
    run_server(host, port, queue)


if __name__ == '__main__':
    fire.Fire({'run-server': run_server_cli})
