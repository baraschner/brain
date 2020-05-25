import fire

from brain.utils import consts
from .saver import Saver


def save(field, filename, database=consts.MONGODB_DEFAULT_URL):
    """
    save parsed data in the database

    :param field: field to save
    :param filename: path to a file that contains the data
    :param database: url of database in which data will be saved
    :return:
    """
    saver = Saver(database)
    with open(filename) as f:
        data = f.read()
    saver.save(field, data)


def run_saver(database=consts.MONGODB_DEFAULT_URL, queue=consts.RABBIT_DEFAULT_URL):
    """
    run saver as a server that consumes data from a queue

    :param database: url of database
    :param queue: url of queue
    :return:
    """
    saver = Saver(database, queue)
    saver.run()


if __name__ == '__main__':
    cli = {'run-saver': run_saver, 'save': save}
    fire.Fire(cli)
