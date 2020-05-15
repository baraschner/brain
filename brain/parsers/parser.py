import importlib
import inspect
import json
import pathlib
import sys

from brain.utils import build_queue_connection_from_url, consts


class Parser:
    def __init__(self, field=None , binary=False, context = None):
        self.field = field
        self.parser = None
        self.supported_fields = []
        self.initialize_parsers(binary,context)

    def initialize_parsers(self):
        root = pathlib.Path(__file__).absolute().parent/'fields'
        sys.path.insert(0, str(root.parent))
        for path in root.iterdir():
            module = importlib.import_module(f'{root.name}.{path.stem}', package=root.name).__dict__
            for item in module.values():
                self.add_parser(item)

    def add_parser(self, obj):
        if inspect.isclass(obj) and 'parse' in obj.__dict__ and consts.FIELD in obj.__dict__:
            self.supported_fields.append(obj.field)
            if obj.field == self.field:
                self.parser = obj().parse
        elif inspect.isfunction(obj) and consts.FIELD in obj.__dict__:
            self.supported_fields.append(obj.field)
            if obj.field == self.field:
                self.parser = obj

    def queue_parse(self, queue_url):
        connection = build_queue_connection_from_url(queue_url)
        connection.exchange_declare(consts.PARSER_INPUT_EXCHANGE_NAME, 'fanout')
        connection.exchange_declare(consts.PARSER_OUTPUT_EXCHANGE_NAME, 'topic')

        def on_message(channel, method_frame, header_frame, body):
            json_data = json.loads(body)
            header = {consts.USER_ID: json_data[consts.USER_ID], consts.DATETIME: json_data[consts.DATETIME]}
            connection.publish(exchange=consts.PARSER_OUTPUT_EXCHANGE_NAME, routing_key=self.field,
                               data=json.dumps({consts.HEADER: header, consts.DATA: self.parser(json_data)}))

        connection.anonymous_queue_declare_and_bind(consts.PARSER_INPUT_EXCHANGE_NAME, on_message)
        connection.start_consuming()

    @staticmethod
    def get_supported_fields():
        return Parser().supported_fields
