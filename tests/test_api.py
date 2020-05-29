import multiprocessing
import time
from pathlib import Path

from pytest import fixture

from brain.api import run_api_server
from brain.cli import *

_SERVER_HOST = "127.0.0.1"
_SERVER_PORT = 5000
_DEPTHIMAGE_PATH = Path(__file__).parent / 'parsers' / 'resources' / 'depthImage.expected'
_USERID = 42
_SNAPSHOT_ID = "5ed10b5776f0aa9affa9e3f0"


@fixture(autouse=True)
def api_fixture(mongodb):
    process = multiprocessing.Process(target=run_api_server,
                                      args=(_SERVER_HOST, _SERVER_PORT, None, mongodb,))
    process.start()
    time.sleep(2)
    try:
        yield
    finally:
        process.kill()


@fixture()
def binary_data():
    with open(_DEPTHIMAGE_PATH, 'rb') as f:
        return f.read()


def test_get_users():
    result = requests.get(f'http://{_SERVER_HOST}:{_SERVER_PORT}/users').json()
    assert result == [{'username': 'Dan Gittik', 'userId': 42}]


def test_get_user():
    result = requests.get(f'http://{_SERVER_HOST}:{_SERVER_PORT}/users/{_USERID}').json()
    assert result == {'userId': 42, 'birthday': 699746400, 'gender': 'MALE', 'username': 'Dan Gittik'}


def test_get_snapshots():
    result = requests.get(f'http://{_SERVER_HOST}:{_SERVER_PORT}/users/{_USERID}/snapshots').json()
    assert result == [{'datetime': 1575446887339, 'id': '5ed10b5776f0aa9affa9e3f0'}]


def test_get_snapshot():
    result = requests.get(f'http://{_SERVER_HOST}:{_SERVER_PORT}/users/{_USERID}/snapshots/{_SNAPSHOT_ID}').json()
    assert result == {'id': '5ed10b5776f0aa9affa9e3f0', 'datetime': 1575446887339,
                      'available fields': ['feelings', 'user', 'pose', 'depthImage', 'colorImage']}


def test_get_field():
    get_result(42, _SNAPSHOT_ID, 'feelings', _SERVER_HOST, _SERVER_PORT)
    result = requests.get(
        f'http://{_SERVER_HOST}:{_SERVER_PORT}/users/{_USERID}/snapshots/{_SNAPSHOT_ID}/feelings').json()
    assert result == {'hunger': 0.0, 'thirst': 0.0, 'exhaustion': 0.0, 'happiness': 0.0}


def test_get_binary_field(binary_data):
    result = requests.get(f'http://{_SERVER_HOST}:{_SERVER_PORT}'
                          f'/users/{_USERID}/snapshots/{_SNAPSHOT_ID}/depthImage/data').content
    assert binary_data == result
