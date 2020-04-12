from brain.protocol.message_base import MessageBase


class ConfigResponse(MessageBase):
    def __init__(self, fields=None):
        self.supported_fields = fields

    def add_supported_field(self, field):
        self.supported_fields.append(field)
