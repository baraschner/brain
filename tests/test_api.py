from pytest import fixture

from brain.api import run_api_server

_SERVER_HOST = "127.0.0.1"
_SERVER_PORT = 5000
_SERVER_URL = "http://127.0.0.1:5000"
_DB_URL = 'mongodb://127.0.0.1:5000'
_SNAPSHOT_ID = "ID"
_FIELD = "FIELD"
_USER_ID = 1337
_RESULT_PRINT = '42\n'
_RESULT = 42


@fixture
def start_api_server():
    run_api_server(_SERVER_HOST, _SERVER_PORT, 'mongodb://127.0.0.1')


'''
def test_get_users(requests_mock, capsys):
    requests_mock.get(f'{_SERVER_URL}/users', json=dumps(_RESULT))
    get_users()
    captured = capsys.readouterr()
    assert captured.out == _RESULT_PRINT


def test_get_user(requests_mock, capsys):
    requests_mock.get(f'{_SERVER_URL}/users/{_USER_ID}', json=dumps(_RESULT))
    get_user(_USER_ID)
    captured = capsys.readouterr()
    assert captured.out == _RESULT_PRINT


def test_get_snapshots(requests_mock, capsys):
    requests_mock.get(f'{_SERVER_URL}/users/{_USER_ID}/snapshots', json=dumps(_RESULT))
    get_snapshots(_USER_ID)
    captured = capsys.readouterr()
    assert captured.out == _RESULT_PRINT


def test_get_snapshot(requests_mock, capsys):
    requests_mock.get(f'{_SERVER_URL}/users/{_USER_ID}/snapshots/{_SNAPSHOT_ID}', json=dumps(_RESULT))
    get_snapshot(_USER_ID, _SNAPSHOT_ID)
    captured = capsys.readouterr()
    assert captured.out == _RESULT_PRINT


def test_result(requests_mock, capsys):
    requests_mock.get(f'{_SERVER_URL}/users/{_USER_ID}/snapshots/{_SNAPSHOT_ID}/{_FIELD}', json=dumps(42))
    get_result(_USER_ID, _SNAPSHOT_ID, _FIELD)
    captured = capsys.readouterr()
    assert captured.out == _RESULT_PRINT
'''
