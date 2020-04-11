import matplotlib.pyplot as plt
import numpy as np


class ColorImageParser:
    field = 'depth_image'

    def __init__(self):
        pass

    def parse(self, data):
        path = self.context.path('depth_image.jpg')
        depth_image = data['depthImage']
        data = np.array(depth_image['data']).reshape((depth_image['height'], depth_image['width']))
        plt.imsave(path, data)
