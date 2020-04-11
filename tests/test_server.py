from brain.utils import consts
import pathlib
from brain.server import run_server
_SERVER_ADDRESS = '127.0.0.1', 5000
_SERVER_PATH = pathlib.Path(__file__).absolute().parent.parent / 'server.py'


def test_api():
    assert 1==1
