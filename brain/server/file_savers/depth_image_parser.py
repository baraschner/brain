
import matplotlib.pyplot as plt
import numpy as np





def parse_depth_image(self, data,context):
    path = context.path('depth_image.jpg')
    depth_image = data['depthImage']
    formated_data = np.array(depth_image['data']).reshape((depth_image['height'], depth_image['width']))
    plt.imsave(path, formated_data)
    data['colorImage'] = str(path)

parse_depth_image.field = 'depthImage'
parse_depth_image.field_type = 'binary'


