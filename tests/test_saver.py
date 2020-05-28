from pathlib import Path

import mongomock
from pytest import fixture
from pymongo import MongoClient
from brain.saver import Saver
from brain.utils import consts

_SAMPLE_PATH = Path('tests/resources/parsed_feelings_queue.json').absolute()
_MONGO_URL = 'mongodb://127.0.0.1:27017'

'''
@fixture(autouse=True)
def mock_db():
    with mongomock.patch(servers=['localhost', 'mongodb']):
        yield


def test_saver():
    saver = Saver(_MONGO_URL)
    with open(_SAMPLE_PATH) as f:
        data = f.read()
    saver.save('feelings', data)
    client = MongoClient(_MONGO_URL).brain
    assert 'feelings' in client.snapshots.find_one()
    
'''
