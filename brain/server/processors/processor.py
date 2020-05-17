import importlib
import inspect
import json
import pathlib
import sys

from brain.utils import build_queue_connection_from_url, consts


class Processor:
    def __init__(self):
        self.processors = {}
        self.initialize_processors()

    def initialize_processors(self):
        root = pathlib.Path(__file__).absolute().parent / 'processors'
        sys.path.insert(0, str(root.parent))
        for path in root.iterdir():
            module = importlib.import_module(f'{root.name}.{path.stem}', package=root.name).__dict__
            for item in module.values():
                self.add_parser(item)

    def add_processor(self, obj):
        if inspect.isclass(obj) and 'process' in obj.__dict__ and consts.FIELD in obj.__dict__:
            self.processors[obj.field] = obj().parse
        elif inspect.isfunction(obj) and consts.FIELD in obj.__dict__:
            self.processors[obj.field] = obj().parse

    def process_data(self, data, context):
        for field, processor in self.processors():
            try:
                processor(data)
            except Exception:
                pass
