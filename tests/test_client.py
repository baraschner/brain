from bson.json_util import loads
from pathlib import Path
from pytest import fixture

from brain.client import upload_sample

_SAMPLE_PATH = Path('tests/resources/sample.mind.gz').absolute()
_HOST = '127.0.0.1'
_PORT = 80
_USER_EXPECTED = {'userId': 42, 'username': "Dan Gittik", 'birthday': 699746400, 'gender': "MALE"}


@fixture()
def config(requests_mock):
    requests_mock.get(f"http://127.0.0.1/config", json={"supported_fields": ['pose', 'feelings']})

@fixture()
def upload(requests_mock):
    requests_mock.post(f"http://127.0.0.1/config")


def test_config(config):
    upload_sample(_SAMPLE_PATH, _HOST, _PORT, test=True)
    data = config.last_request.body
    assert 'pose' in data and 'feelings' in data and 'depthImage' not in data

def test_upload(upload):
    upload_sample(_SAMPLE_PATH, _HOST, _PORT, test=True)
    data = config.last_request.body
    assert data['user'] == _USER_EXPECTED



