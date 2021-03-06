import pika
from furl import furl


def build_queue_connection_from_url(url):
    """
    Takes url in the form [QUEUE_TYPE]://[host]:port, the rest of the url will be ignored.

    :param url: string that specifies the url
    :return: QueueConnector object built from url
    """
    url = furl(url)
    if url.scheme == 'rabbitmq':
        return RabbitMQConnector(url.host, url.port)
    else:
        raise Exception("Queue Type not Supported")


class RabbitMQConnector:
    """
    Connector class that supports RabbitMQ
    """

    def __init__(self, host, port):
        params = pika.ConnectionParameters(host=host, port=port, heartbeat=600, blocked_connection_timeout=300)
        self.con = pika.BlockingConnection(params)
        self.channel = self.con.channel()
        self.queue = None

    def exchange_declare(self, exchange, exchange_type):
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)

    def publish(self, exchange, data, routing_key=''):
        self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=data)

    def anonymous_queue_declare_and_bind(self, exchange_name, callback, routing_key=''):
        """
        Creates anonymous queue, binds it to an exchange and registers a callback

        :param exchange_name:
        :param callback:
        :param routing_key:
        :return:
        """
        self.queue = self.channel.queue_declare(queue='', exclusive=True).method.queue
        self.channel.queue_bind(exchange=exchange_name, queue=self.queue, routing_key=routing_key)
        self.channel.basic_consume(queue=self.queue, on_message_callback=callback, auto_ack=True)

    def start_consuming(self):
        """
        Start consuming messages from the registered queue.

        :return:
        """
        self.channel.start_consuming()
