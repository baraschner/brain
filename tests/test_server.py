import json
import multiprocessing
import time
from pathlib import Path

import requests
from pytest import fixture

from brain.client import upload_sample
from brain.server import run_server

_SAMPLE_PATH = Path('tests/resources/sample.mind.gz').absolute()
_SERVER_IP = '127.0.0.1'
_SERVER_TEST_PORT = 8000
_EXPECTED_SUPPORTED = ['feelings', 'pose', 'user', 'depthImage', 'colorImage']


@fixture()
def server_fixture(publish_fixture):
    func, path = publish_fixture
    process = multiprocessing.Process(target=run_server,
                                      args=(_SERVER_IP, _SERVER_TEST_PORT, None, func, path.absolute(),))
    process.start()
    time.sleep(2)
    try:
        yield path
    finally:
        process.kill()


@fixture()
def publish_fixture(tmp_path):
    def on_message(m):
        with open(tmp_path / 'result', 'w') as f:
            f.write(m)

    yield on_message, tmp_path


def test_config(server_fixture):
    result = json.loads(requests.get(f'http://{_SERVER_IP}:{_SERVER_TEST_PORT}/config').json())
    assert all(k in result['supported_fields'] for k in _EXPECTED_SUPPORTED)


def test_snapshot(server_fixture):
    upload_sample(_SAMPLE_PATH, _SERVER_IP, _SERVER_TEST_PORT)
    with open(server_fixture / 'result') as f:
        d = json.load(f)
    assert 'userId' in d and 'feelings' in d
