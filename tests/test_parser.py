import json
from pytest import fixture
from pathlib import Path
from brain.parsers import Parser, run_parser

_PARSE_RESULT = Path('tests/data/parsed_feelings_raw.json').absolute()
_PARSE_QUEUE_RESULT = None
_PARSE_DATA = Path('tests/data/snapshot.json').absolute()


@fixture()
def data():
    with open(_PARSE_DATA) as f:
        return json.loads(f.read())


def test_parser(data):
    result = run_parser('feelings', data)
    with open(_PARSE_RESULT) as f:
        assert sorted(result.items()) == sorted(json.load(f).items())

