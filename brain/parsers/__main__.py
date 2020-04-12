import json

import fire

from .parser import Parser
from brain.utils import consts


def parse(field, snapshot_file):
    """
    parses the field from file
    :param field: field to parse
    :param snapshot_file: path to a file that contains a snapshot
    :return:
    """
    parser = Parser(field)
    with open(snapshot_file) as f:
        data = f.read()

    json_data = json.loads(data)
    print(parser.parser(json_data))


def run_parser(field, queue):
    """
    run parser as server that consumes a queue.
    :param field: field to parse
    :param queue: url of message queue
    :return:
    """
    parser = Parser(field)
    parser.queue_parse(queue)


if __name__ == '__main__':
    cli = {"run-parser": run_parser, "parse": parse}
    fire.Fire(cli)
