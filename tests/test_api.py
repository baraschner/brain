from pathlib import Path

from pytest import fixture

from brain.api import run_api_server

_SERVER_HOST = "127.0.0.1"
_SERVER_PORT = 5000
_DEPTHIMAGE_PATH = Path(__file__).parent / 'parsers' / 'resources' / 'depthImage.expected'
_USERID = 42
_SNAPSHOT_ID = "5ed10b5776f0aa9affa9e3f0"


@fixture()
def api_fixture(mongodb):
    app = run_api_server(_SERVER_HOST, _SERVER_PORT, db=mongodb, test=True)
    return app.test_client()


def test_get_users(api_fixture):
    result = api_fixture.get(f'/users').json
    assert result == [{'username': 'Dan Gittik', 'userId': 42}]


def test_get_user(api_fixture):
    result = api_fixture.get(f'/users/{_USERID}').json
    assert result == {'userId': 42, 'birthday': 699746400, 'gender': 'MALE', 'username': 'Dan Gittik'}


def test_get_snapshots(api_fixture):
    result = api_fixture.get(f'/users/{_USERID}/snapshots').json
    assert result == [{'datetime': 1575446887339, 'id': '5ed10b5776f0aa9affa9e3f0'}]


def test_get_snapshot(api_fixture):
    result = api_fixture.get(f'/users/{_USERID}/snapshots/{_SNAPSHOT_ID}').json
    assert result == {'id': '5ed10b5776f0aa9affa9e3f0', 'datetime': 1575446887339,
                      'available fields': ['feelings', 'user', 'pose', 'depthImage', 'colorImage']}


def test_get_field(api_fixture):
    result = api_fixture.get(
        f'/users/{_USERID}/snapshots/{_SNAPSHOT_ID}/feelings').json
    assert result == {'hunger': 0.0, 'thirst': 0.0, 'exhaustion': 0.0, 'happiness': 0.0}
