import json

import fire

from .parser import Parser
from brain.utils import consts

def parse(field, snapshot_file):
    parser = Parser(field)
    with open(snapshot_file) as f:
        data = f.read()

    json_data = json.loads(data)
    print(parser.parser(json_data))


def run_parser(field, queue):
    parser = Parser(field)
    parser.queue_parse(queue)


if __name__ == '__main__':
    cli = {"run-parser": run_parser, "parse": parse}
    fire.Fire(cli)
