from pytest import fixture

import json
import requests
import multiprocessing
import time
from pathlib import Path

from brain.server import run_server
from brain.client import upload_sample
from brain.utils import consts
_SAMPLE_PATH = Path('tests/data/sample.mind.gz').absolute()


@fixture()
def server_fixture(publish):
    func,path = publish
    process = multiprocessing.Process(target=run_server, args=('127.0.0.1', 4080, None, func,))
    process.start()
    time.sleep(2)
    try:
        yield path
    finally:
        process.kill()


@fixture()
def publish(tmp_path):

    def on_message(m):
        with open(tmp_path/'result','w') as f:
            f.write(m)
    yield on_message,tmp_path


def test_config(server_fixture):
    result = json.loads(requests.get('http://127.0.0.1:4080/config').json())
    assert 'feelings' in result['supported_fields']


def test_snapshot(server_fixture):
    upload_sample(_SAMPLE_PATH, '127.0.0.1', 4080)
    with open(server_fixture/'result') as f:
        d = json.load(f)
    assert 'userId' in d and 'feelings' in d
