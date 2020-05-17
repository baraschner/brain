import requests

from brain.utils import consts


def get_users(host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT):
    print(requests.get(f'http://{host}:{port}/users').json())


def get_user(user_id, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT):
    print(requests.get(f'http://{host}:{port}/users/{user_id}').json())


def get_snapshots(user_id, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT):
    print(requests.get(f'http://{host}:{port}/users/{user_id}/snapshots').json())


def get_snapshot(user_id, snapshot_id, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT):
    print(requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}').json())


def get_result(user_id, snapshot_id, result, host=consts.LOCALHOST, port=consts.DEFAULT_API_PORT, save=None):
    if save:
        result = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}/data')
        with open(save, 'wb') as f:
            f.write(result.content)
    else:
        result = requests.get(f'http://{host}:{port}/users/{user_id}/snapshots/{snapshot_id}/{result}').json()
        print(result)


cli_dict = {'get-users': get_users,
            'get-user': get_user,
            'get-snapshots': get_snapshots,
            'get-snapshot': get_snapshot,
            'get-result': get_result}
