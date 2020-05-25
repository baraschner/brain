import fire

from brain.utils import consts
from .server import run_server


def run_gui_server_cli(host=consts.LOCALHOST, port=consts.DEFAULT_UI_PORT, api_host=consts.LOCALHOST,
                       api_port=consts.DEFAULT_API_PORT):
    """
    runs the server on a given host and port with the message queue provided.
    :param host: ip address of host
    :param port: port to bind the server
    :param api_host: ip address of api server
    :param api_port: port of api server
    """
    run_server(host, port, api_host, api_port)


if __name__ == '__main__':
    fire.Fire({'run-server': run_gui_server_cli})
