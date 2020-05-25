import json
from pathlib import Path

from pytest import fixture

from brain.parsers import run_parser

_PARSE_RESULT = Path('tests/resources/parsed_feelings_raw.json').absolute()
_PARSE_QUEUE_RESULT = None
_PARSE_DATA = Path('tests/resources/snapshot.json').absolute()


@fixture()
def data():
    with open(_PARSE_DATA) as f:
        return json.loads(f.read())


def test_parser(data):
    result = run_parser('feelings', data)
    with open(_PARSE_RESULT) as f:
        assert sorted(result.items()) == sorted(json.load(f).items())
