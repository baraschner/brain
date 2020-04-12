import mongomock
from pathlib import Path
from brain.saver import Saver
from brain.utils import consts

_SAMPLE_PATH = Path('tests/data/parsed_feelings_queue.json').absolute()
_MONGO_URL = 'mongodb://a.com:27017'
'''
@mongomock.patch(servers=(('server.example.com', 27017),))
def test_saver():
    saver = Saver('mongodb://server.example.com:27017')
    with open(_SAMPLE_PATH) as f:
        data = f.read()
    saver.save('feelings', data)
    assert saver.client[consts.db_name].snapshots.find_one()==3
'''
