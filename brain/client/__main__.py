import fire

from .client import Client



def upload_cli(host,port, file):
    client = Client(host,port, file)
    client.upload()


if __name__ == '__main__':
    fire.Fire(upload_cli)
