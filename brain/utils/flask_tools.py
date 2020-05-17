import importlib
import inspect
import pathlib
import sys

from brain.utils import consts


def api_driver(api, path, resource_class_args=()):
    """
    initializes an api dynamically according to their endpoint field

    :param path: the path from which to load the modules
    :param resource_class_args: parameters that will be provided to class constructors
    :param api: flask api to which endpoints will be added
    :return:
    """
    root = pathlib.Path(path).parent.absolute() / consts.API_RESOURCES_MODULE_PATH
    sys.path.insert(0, str(root))
    for file in root.iterdir():
        attrs = importlib.import_module(file.stem, package=consts.API_RESOURCES_MODULE_PATH).__dict__.values()
        for resource in filter(lambda obj: inspect.isclass(obj) and consts.URL_FIELD in obj.__dict__, attrs):
            api.add_resource(resource, resource.__dict__[consts.URL_FIELD], resource_class_args=resource_class_args)
