import datetime as dt
import pathlib

_SERVER_ADDRESS = '127.0.0.1', 5000
_SERVER_PATH = pathlib.Path(__file__).absolute().parent.parent / 'server.py'

_HEADER_FORMAT = 'LLI'

_USER_1 = 1
_USER_2 = 2
_TIMESTAMP_1 = int(dt.datetime(2019, 10, 25, 15, 12, 5, 228000).timestamp())
_TIMESTAMP_2 = int(dt.datetime(2019, 10, 25, 15, 15, 2, 304000).timestamp())
_THOUGHT_1 = "I'm hungry"
_THOUGHT_2 = "I'm sleepy"


def test_thing():
    assert 1 == 1
