import base64
import os
import json
from PIL import Image as PIL


def parse_color_image(data):
    path = data['colorImage']['path']
    with open(path) as f:
        d = json.load(f)

    os.remove(path)

    raw_data = d['data']
    size = d['width'], d['height']

    image = PIL.new('RGB', size)
    decoded = base64.b64decode(raw_data)
    image.putdata([(decoded[i], decoded[i + 1], decoded[i + 2]) for i in range(0, len(decoded), 3)])

    image.save(path)

    result = {'path': path, 'content-type': 'image/jpg'}
    return result


parse_color_image.field = 'colorImage'
