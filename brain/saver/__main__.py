import fire

from .saver import Saver
from brain.utils import consts


def save(field, filename, db=consts.MONGODB_DEFAULT_URL):
    saver = Saver(db)
    with open(filename) as f:
        data = f.read()
    saver.save(field, data)


def run_saver(database=consts.MONGODB_DEFAULT_URL, queue=consts.RABBIT_DEFAULT_URL):
    saver = Saver(database, queue)
    saver.run()


if __name__ == '__main__':
    cli = {'run-saver': run_saver, 'save': save}
    fire.Fire(cli)
