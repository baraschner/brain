import json
from .parser import Parser


def parse(field, snapshot_file):
    """
    parses the field from file

    :param field: field to parse
    :param snapshot_file: path to a file that contains a snapshot
    :return:
    """
    with open(snapshot_file) as f:
        data = f.read()

    print(run_parser(field, json.loads(data)))


def run_parser(field, data):
    return Parser(field).parser(data)


def run_queue_parser(field, queue_url):
    """
    run parser as server that consumes a queue.
    :param field: field to parse
    :param queue: url of message queue
    :return:
    """
    parser = Parser(field)
    parser.queue_parse(queue_url)
