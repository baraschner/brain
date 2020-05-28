import json

from .consts import DUMP_FIELDS


def dump_binary_data(data, context):
    """
    Dump binary data that is sent to the server to disk, to later be consumed by parsers.
    :param data: data from which we will dump
    :param context: context object used to determine the path to save
    :return:
    """
    for field in DUMP_FIELDS:
        path = context.path(field)
        with open(path, 'w') as f:
            json.dump(data[field], f)
            data[field] = {'path': str(path)}
