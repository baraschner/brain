import json
import os

import matplotlib.pyplot as plt
import numpy as np


def parse_depth_image(data):
    path = data['depthImage']['path']
    with open(path) as f:
        d = json.load(f)

    os.remove(path)

    depth_image = d['data']
    height = d['height']
    width = d['width']
    formatted_data = np.array(depth_image).reshape((height, width))

    save_path = path + '.jpg'

    plt.imsave(save_path, formatted_data)

    result = {'path': save_path, 'content-type': 'image/jpg'}
    return result


parse_depth_image.field = 'depthImage'
