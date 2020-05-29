import fire

from brain.utils import consts
from .api import run_api_server


def run_server(host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, database=consts.MONGODB_DEFAULT_URL):
    """
    run the api server
    :param host: ip to bind
    :param port: port to bind
    :param database: database from which we'll get the data
    :return:
    """
    run_api_server(host, port, database, None)


if __name__ == '__main__':
    fire.Fire({'run-server': run_server})
