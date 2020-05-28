import json

from brain.utils import consts


def parser_serialize(data_dict, parsed_data):
    header = {consts.USER_ID: data_dict[consts.USER_ID], consts.DATETIME: data_dict[consts.DATETIME]}
    return json.dumps({consts.HEADER: header, consts.DATA: parsed_data})


def saver_deserialize(data):
    data_dict = json.loads(data)
    save_data = data_dict[consts.DATA]
    user_id = data_dict[consts.HEADER][consts.USER_ID]
    datetime = data_dict[consts.HEADER][consts.DATETIME]
    return user_id, datetime, save_data
