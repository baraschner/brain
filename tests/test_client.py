from brain.utils import consts
from brain.client import upload_sample

from pathlib import Path
from bson import BSON
from json import load as json_load
from json import dumps as json_dumps

_ROOT_PATH = Path(__file__).absolute().parent.parent / 'server.py'
_SAMPLE_PATH = Path('tests/data/sample.mind.gz').absolute()
_DATA_JSON = Path('tests/data/snapshot.json').absolute()

_SERVER_URL = f'http://{consts.SERVER_DEFAULT_HOST}:{consts.SERVER_DEFAULT_PORT}'
_SUPPORTED_FIELDS = {
    "supported_fields": [consts.POSE, consts.COLOR_IMAGE, consts.DEPTH_IMAGE, consts.FEELINGS]}


def test_upload_sample(requests_mock):
    requests_mock.get(f'{_SERVER_URL}/config', json=json_dumps(_SUPPORTED_FIELDS))
    requests_mock.post(f'{_SERVER_URL}/snapshot')
    upload_sample(_SAMPLE_PATH, test=True)
    data_recv = BSON.decode(requests_mock.last_request.body)

    with open(_DATA_JSON, 'r') as f:
        json_load(f)

    data = data_recv
    assert sorted(data_recv.items()) == sorted(data.items())
