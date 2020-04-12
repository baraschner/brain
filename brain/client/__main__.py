import fire

from .client import Client



def upload_cli(host,port, file):
    """

    :param host: ip of server
    :param port: port of server
    :param file: file in format mind.gz that contains the sample
    :return:
    """
    client = Client(host,port, file)
    client.upload()


if __name__ == '__main__':
    fire.Fire(upload_cli)
