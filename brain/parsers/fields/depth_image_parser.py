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
    save_path = path + '.jpg'

    height = d['height']
    width = d['width']
    formatted_data = np.array(depth_image).reshape((height, width))
    plt.imsave(save_path, formatted_data)

    result = {'path': save_path, 'content-type': 'image/jpg'}
    return result


parse_depth_image.field = 'depthImage'
