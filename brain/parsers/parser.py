import json

from brain.utils import build_queue_connection_from_url, consts, parser_serialize


class QueueParser:
    def __init__(self, parse_function, queue_url, field):
        self.function = parse_function
        self.queue_url = queue_url
        self.field = field

    def queue_parse(self):
        connection = build_queue_connection_from_url(self.queue_url)
        connection.exchange_declare(consts.PARSER_INPUT_EXCHANGE_NAME, 'fanout')
        connection.exchange_declare(consts.PARSER_OUTPUT_EXCHANGE_NAME, 'topic')

        def on_message(channel, method_frame, header_frame, body):
            data_dict = json.loads(body)
            result = self.function(data_dict)

            connection.publish(exchange=consts.PARSER_OUTPUT_EXCHANGE_NAME, routing_key=self.field,
                               data=parser_serialize(data_dict, result))

        connection.anonymous_queue_declare_and_bind(consts.PARSER_INPUT_EXCHANGE_NAME, on_message)
        connection.start_consuming()
