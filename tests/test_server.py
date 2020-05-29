from pathlib import Path

from pytest import fixture

from brain.server import run_server

RESOURCES = Path(__file__).parent / 'resources'

_SAMPLE_PATH = RESOURCES / 'sample.mind.gz'
_SERVER_IP = '127.0.0.1'
_SERVER_TEST_PORT = 8000
_EXPECTED_SUPPORTED = ['feelings', 'pose', 'user', 'depthImage', 'colorImage']


def publish(m):
    return m


@fixture()
def server_fixture(tmp_path):
    app = run_server(_SERVER_IP, _SERVER_TEST_PORT, publish=publish, base_save_path=tmp_path, test=True)
    return app.test_client()


def test_config(server_fixture):
    result = server_fixture.get('/config').json
    assert all(k in result['supported_fields'] for k in _EXPECTED_SUPPORTED)


'''
def test_snapshot(server_fixture):
    upload_sample(_SAMPLE_PATH,test=server_fixture)
    with open(server_fixture / 'result') as f:
        d = json.load(f)
    assert 'userId' in d and 'feelings' in d
    '''
