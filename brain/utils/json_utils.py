def filter_json(js, fields):
    filtered = {}
    for elem in fields:
        filtered[elem] = js[elem]
    return filtered
