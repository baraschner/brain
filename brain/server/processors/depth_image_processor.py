import json


def process_depth_image(data, context):
    path = context.path('depth_image.jpg')

    with open(path, 'w') as f:
        json.dump(data['depthImage'], f)

    data['depthImage'] = {'path': str(path)}


process_depth_image.field = 'depthImage'
process_depth_image.field_type = 'binary'
