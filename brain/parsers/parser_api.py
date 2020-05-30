import json

from brain.utils import consts
from .parser_factory import get_parser
from .queueparser import QueueParser


def parse(field, snapshot_file):
    """
    parses the field from file

    :param field: field to parse
    :param snapshot_file: path to a file that contains a snapshot
    :return:
    """
    with open(snapshot_file) as f:
        data = json.load(f)

    print(run_parser(field, data))


def run_parser(field, data):
    """
    parse data according to specific field and return the result

    :param field: field to parse
    :param data: data to parse
    :return: result of parser
    """
    return get_parser(field)(data)


def run_queue_parser(field, queue=consts.RABBIT_DEFAULT_URL):
    """
    run parser as server that consumes a queue.

    :param field: field to parse
    :param queue: url of message queue
    :return:
    """
    parser = QueueParser(get_parser(field), queue, field)
    parser.queue_parse()
