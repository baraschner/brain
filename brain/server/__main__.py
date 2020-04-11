import click

from .server import run


@click.command()
@click.option('--address', default="127.0.0.1:8000",
              help='Server address in [HOST]:[PORT] format. Default is 127.0.0.1:8000')
@click.option('--url', help='datadir', required=True)
def run_server(address, url):
    addr = address.split(":")
    run(addr[0], addr[1], url)


if __name__ == '__main__':
    run_server()
