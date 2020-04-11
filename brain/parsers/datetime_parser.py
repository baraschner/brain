from datetime import datetime

from brain.utils import datetime_string_format


def parser(data_json):
    ts = int(data_json['datetime']) / 1000
    date = datetime_string_format(str(datetime.fromtimestamp(ts)))
    return date


parser.field = 'datetime'
