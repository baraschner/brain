import click

from .client import Client


@click.command()
@click.option('--address', default="127.0.0.1:8000",
              help='Server address in [HOST]:[PORT] format. Default is 127.0.0.1:8000')
@click.option('--file', help='Thought filename', required=True)
def upload_cli(host,port, file):
    client = Client(host,port, file)
    client.upload()


if __name__ == '__main__':
    upload_cli()
