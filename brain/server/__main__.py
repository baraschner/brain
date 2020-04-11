import fire

from .server import run_server
from brain.utils import consts


def run_server(host=consts.LOCALHOST,port=consts.SERVER_DEFAULT_PORT, queue_url=consts.RABBIT_DEFAULT_URL):
    run_server(host, port, queue_url)


if __name__ == '__main__':
    fire.Fire({'run-server':run_server})
