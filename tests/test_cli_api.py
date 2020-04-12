from brain.utils import consts
from brain.cli import *

import pathlib
from json import dumps
from io import StringIO

_SERVER_URL = "http://127.0.0.1:5000"
_SERVER_PATH = pathlib.Path(__file__).absolute().parent.parent / 'server.py'
_SNAPSHOT_ID = "ID"
_FIELD = "FIELD"
_USER_ID = 1337


def test_get_users(requests_mock):
    io = StringIO()
    requests_mock.get(f'{_SERVER_URL}/users', json=dumps(42))
    get_users()
    #assert captured.out == '42'

'''
def test_get_user(requests_mock):
    io = StringIO()
    requests_mock.get(f'{_SERVER_URL}/users/{_USER_ID}', json=dumps(42))
    get_user(_USER_ID, save=io)
    assert io.getvalue() == '42'


def test_get_snapshots(requests_mock):
    io = StringIO()
    requests_mock.get(f'http://{_SERVER_URL}/users/{_USER_ID}/snapshots', json=dumps(42))
    get_snapshots(_USER_ID, save=io)
    assert io.getvalue() == '42'


def test_get_snapshot(requests_mock):
    io = StringIO()
    requests_mock.get(f'http://{_SERVER_URL}/users/{_USER_ID}/snapshots/{_SNAPSHOT_ID}', json=dumps(42))
    get_snapshots(_USER_ID, _SNAPSHOT_ID, save=io)
    assert io.getvalue() == '42'


def test_result(requests_mock):
    io = StringIO()
    requests_mock.get(f'http://{_SERVER_URL}/users/{_USER_ID}/snapshots/{_SNAPSHOT_ID}/{_FIELD}', json=dumps(42))
    get_result(_USER_ID, _SNAPSHOT_ID, _FIELD, save=io)
    assert io.getvalue() == '42'
'''
