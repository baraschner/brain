from brain.utils import consts
import requests


def output(data, save):
    if save:
        with open(save, 'w') as f:
            f.write(data)
    else:
        print(data)


def get_users(host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, save=None):
    result = requests.get(f'http://{host}:{port}/users')
    output(result, save)


def get_user(user_id, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, save=None):
    result = requests.get(f'http://{host}:{port}/users/{user_id}')
    output(result, save)


def get_snapshots(user_id, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, save=None):
    result = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots')
    output(result, save)


def get_snapshot(user_id, snapshot_id, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, save=None):
    result = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}')
    output(result, save)


def get_result(user_id, snapshot_id, result, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, save=None):
    result = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}')
    output(result, save)


cli_dict = {'get-users': get_users,
            'get-user': get_user,
            'get-snapshots': get_snapshot,
            'get-snapshot': get_snapshot,
            'get-result': get_result}
