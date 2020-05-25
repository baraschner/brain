import json
import os

import matplotlib.pyplot as plt
import numpy as np


def parse_depth_image(data):
    path = data['depthImage']['path']
    with open(path) as f:
        d = json.load(f)

    depth_image = d['data']
    os.remove(path)

    height = d['height']
    width = d['width']
    formatted_data = np.array(depth_image).reshape((height, width))
    plt.imsave(path, formatted_data)

    result = {'path': path, 'content-type': 'image/jpg'}
    return result


parse_depth_image.field = 'depthImage'
