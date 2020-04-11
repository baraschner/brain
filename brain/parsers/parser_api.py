import json
from .parser import Parser


def parse(field, snapshot_file):
    with open(snapshot_file) as f:
        data = f.read()

    print(run_parser(field, json.loads(data)))


def run_parser(field, data):
    return Parser(field).parser(data)


def run_queue_parser(field, queue_url):
    parser = Parser(field)
    parser.queue_parse(queue_url)
