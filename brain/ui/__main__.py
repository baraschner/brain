import fire

from brain.utils import consts
from .ui import run_ui_server


def run_ui_server_cli(host=consts.LOCALHOST, port=consts.DEFAULT_UI_PORT
                      , api=f"http://{consts.LOCALHOST}:{consts.DEFAULT_API_PORT}"):
    """
    runs the server on a given host and port with the message queue provided.
    :param host: ip address of host
    :param port: port to bind the server
    :param api: ip address of api server

    """
    run_ui_server(host, port, api)


if __name__ == '__main__':
    fire.Fire({'run-server': run_ui_server_cli})
