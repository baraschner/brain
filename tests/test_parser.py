import filecmp
import json
from pathlib import Path

from pytest import fixture, mark

from brain.parsers import run_parser
from brain.utils import Context
from brain.utils import consts, dumper

RESOURCES = Path(__file__).parent / 'resources'

_PARSE_RESULT_BASE = Path(__file__).parent / 'resources' / 'parser_resources'
_PARSE_QUEUE_RESULT = None
_PARSE_DATA = RESOURCES / 'snapshot.json'

_SIMPLE_FIELDS = ['feelings', 'pose', 'user']


@fixture()
def data():
    with open(_PARSE_DATA) as f:
        return json.load(f)


@fixture()
def dumper_fixture(data, tmp_path):
    context = Context(tmp_path, 0, 0)
    dumper.dump_binary_data(data, context)
    return data, context, tmp_path


@mark.parametrize("field", _SIMPLE_FIELDS)
def test_simple_parser(field, data):
    result = run_parser(field, data)
    with open(_PARSE_RESULT_BASE / f"{field}.expected") as f:
        compare = json.load(f)
    assert result == compare


@mark.parametrize("field", consts.DUMP_FIELDS)
def test_binary_parser_return_value(field, dumper_fixture):
    data, context, path = dumper_fixture
    result = run_parser(field, data)
    assert result['content-type'] == 'image/jpg'
    assert result['path'] == str(path / '0' / '0' / f'{field}.jpg')


@mark.parametrize("field", consts.DUMP_FIELDS)
def test_binary_parser(field, dumper_fixture):
    data, context, path = dumper_fixture
    result = run_parser(field, data)
    assert filecmp.cmp(_PARSE_RESULT_BASE / f"{field}.expected", result['path'])
