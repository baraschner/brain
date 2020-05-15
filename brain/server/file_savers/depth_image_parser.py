
import matplotlib.pyplot as plt
import numpy as np





def parse_depth_image(self, data,context):
    path = context.path('depth_image.jpg')
    depth_image = data['depthImage']
    data = np.array(depth_image['data']).reshape((depth_image['height'], depth_image['width']))
    plt.imsave(path, data)

parse_depth_image.field = 'color_image'
parse_depth_image.field_type = 'binary'


