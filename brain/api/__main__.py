import fire

from brain.utils import consts
from .api import *


def run_server(address="127.0.0.1:5000", url=consts.MONGODB_DEFAULT_URL):
    addr = address.split(":")
    run(addr[0], addr[1], url)


if __name__ == '__main__':
    fire.Fire({'run-server': run_server})
