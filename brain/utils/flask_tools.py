import importlib
import inspect
import pathlib
import sys

from brain.utils import consts


def api_driver(api, path, resource_class_arg=None):
    """
    This function initializes the api automatically according to their endpoint field
    :param path: the path from which to load the modules
    :param resource_class_arg: a parameter that will be provided to class constructors
    :param api: flask api to which endpoints will be added
    :return: void
    """
    root = pathlib.Path(path).parent.absolute() / consts.API_RESOURCES_MODULE_PATH
    sys.path.insert(0, str(root))
    for path in root.iterdir():
        module = importlib.import_module(f'{path.stem}',
                                         package=f'{consts.API_RESOURCES_MODULE_PATH}').__dict__
        for item in module.values():
            if inspect.isclass(item) and consts.URL_FIELD in item.__dict__:
                if resource_class_arg is not None:
                    api.add_resource(item, item.__dict__[consts.URL_FIELD], resource_class_args=(resource_class_arg,))
                else:
                    api.add_resource(item, item.__dict__[consts.URL_FIELD])
