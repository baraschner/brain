import json
from pathlib import Path

from bson import BSON
from pytest import fixture

from brain.client import upload_sample

RESOURCES = Path(__file__).parent / 'resources'
_SAMPLE_PATH = RESOURCES / 'sample.mind.gz'
_SNAPSHOT_PATH = RESOURCES / 'snapshot.json'

_HOST = '127.0.0.1'
_PORT = 8000
_USER_EXPECTED = {'userId': 42, 'username': "Dan Gittik", 'birthday': 699746400, 'gender': "MALE"}
_CONFIG = json.dumps({"supported_fields": ['pose', 'feelings']})
_CONFIG_ALL = json.dumps({"supported_fields": ['pose', 'feelings', 'depthImage', 'colorImage']})


@fixture()
def upload_fixture(requests_mock):
    requests_mock.get(f"http://127.0.0.1:8000/config", json=_CONFIG)
    requests_mock.post(f"http://127.0.0.1:8000/snapshot")
    return requests_mock


@fixture()
def upload_all_fixture(requests_mock):
    requests_mock.get(f"http://127.0.0.1:8000/config", json=_CONFIG_ALL)
    requests_mock.post(f"http://127.0.0.1:8000/snapshot")
    return requests_mock


def test_config(upload_fixture):
    upload_sample(_SAMPLE_PATH, _HOST, _PORT, test=True)
    data = BSON.decode(upload_fixture.last_request.body)
    assert 'pose' in data and 'feelings' in data and 'depthImage' not in data


def test_upload(upload_all_fixture):
    upload_sample(_SAMPLE_PATH, _HOST, _PORT, test=True)
    data = BSON.decode(upload_all_fixture.last_request.body)
    with open(_SNAPSHOT_PATH, 'r') as f:
        snapshot = json.load(f)
    assert snapshot == data
