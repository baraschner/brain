
import base64

from PIL import Image as PIL

def parse_color_image(data,context):
    path = context.path('color_image.jpg')
    size = data['colorImage']['width'], data['colorImage']['height']
    image = PIL.new('RGB', size)
    raw_data = base64.b64decode(data['colorImage']['data'])
    image.putdata([(raw_data[i], raw_data[i + 1], raw_data[i + 2]) for i in range(0, len(raw_data), 3)])
    data['colorImage'] = str(path)
    image.save(path)

    parse_color_image.field = 'colorImage'
    parse_color_image.field_type = 'binary'

