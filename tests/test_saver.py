from pathlib import Path

import mongomock
import pytest

RESOURCES = Path(__file__).parent / 'resources'
_SAMPLE_PATH = RESOURCES / 'parsed_feelings_queue.json'
_USER_PATH = RESOURCES / 'parsed_user_queue.json'

_MONGO_URL = 'mongodb://mongodb:27017'


@pytest.fixture(autouse=True)
def mock_db():
    with mongomock.patch(servers=["localhost", "mongodb"]):
        yield


def test_regular_field():
    from brain.saver import Saver

    saver = Saver(_MONGO_URL)
    with open(_SAMPLE_PATH) as f:
        data = f.read()
    saver.save('feelings', data)
    assert 'feelings' in saver.db.snapshots.find_one({})


def test_save_user_data():
    from brain.saver import Saver

    saver = Saver(_MONGO_URL)
    with open(_USER_PATH) as f:
        data = f.read()
    saver.save('user', data)
    assert 'username' in saver.db.users.find_one({})
