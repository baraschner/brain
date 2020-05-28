import importlib
import inspect
import pathlib
import sys

from brain.utils import consts


def find_parsers():
    """
    Driver that finds all parsers
    Parsers are created automatically from modules in the ./fields directory.
    A parser is either:
    A function that contains the "field" property
    A class with field property, parse function, and constructor without any arguments.
    :return: dict of all parsers in the format field:function
    """

    result = {}
    root = pathlib.Path(__file__).absolute().parent / 'fields'
    sys.path.insert(0, str(root.parent))
    for path in root.iterdir():
        module = importlib.import_module(f'{root.name}.{path.stem}', package=root.name).__dict__
        for item in module.values():
            add_parser(result, item)

    return result


def add_parser(parser_dict, obj):
    """
    Imports a parser from a module.

    :param parser_dict: dict of parsers to init
    :param obj: imported module from which should try to add a parser
    :return:
    """
    if inspect.isclass(obj) and 'parse' in obj.__dict__ and consts.FIELD in obj.__dict__:
        parser_dict[obj.field] = obj().parse
    elif inspect.isfunction(obj) and consts.FIELD in obj.__dict__:
        parser_dict[obj.field] = obj


def get_supported_fields():
    return list(find_parsers().keys())


def get_parser(field):
    """
    Creates a parser object according to a field
    :param field: string of the field for which we create the parser
    :return:
    """
    return find_parsers()[field]
