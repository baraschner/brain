import base64
import json
import os

from PIL import Image


def parse_color_image(data):
    path = data['colorImage']['path']
    with open(path) as f:
        d = json.load(f)

    os.remove(path)

    save_path = path+'.jpg'
    raw_data = d['data']
    size = d['width'], d['height']

    image = Image.new('RGB', size)
    decoded = base64.b64decode(raw_data)
    image.putdata([(decoded[i], decoded[i + 1], decoded[i + 2]) for i in range(0, len(decoded), 3)])

    image.save(save_path)

    result = {'path': save_path, 'content-type': 'image/jpg'}
    return result


parse_color_image.field = 'colorImage'
