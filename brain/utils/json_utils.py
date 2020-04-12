def filter_json(js, fields):
    """
    Take only rhe require fields from a dictionary
    :param js:
    :param fields:
    :return:
    """
    filtered = {}
    for elem in fields:
        filtered[elem] = js[elem]
    return filtered
