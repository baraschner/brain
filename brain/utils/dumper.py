import json

DUMP_FIELDS = ['colorImage', 'depthImage']


def dump_field(data, context, field):
    path = context.path(field)

    with open(path, 'w') as f:
        json.dump(data[field], f)

    data[field] = {'path': str(path)}


def dump_binary_data(data, context):
    for field in DUMP_FIELDS:
        dump_field(data, context, field)

