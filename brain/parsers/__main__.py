import fire

from .parser_api import run_queue_parser, parse

if __name__ == '__main__':
    cli = {"run-parser": run_queue_parser, "parse": parse}
    fire.Fire(cli)
