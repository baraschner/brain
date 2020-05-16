import json

def process_color_image(data, context):
    path = context.path('color_image.jpg')

    with open(path, 'w') as f:
        json.dump(data['colorImage'], f)

    data['colorImage'] = {'path': str(path)}


process_color_image.field = 'colorImage'
process_color_image.field_type = 'binary'
