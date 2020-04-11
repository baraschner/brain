from brain.protocol.message_base import MessageBase


class SnapshotMessage(MessageBase):
    def __init__(self, fields=None):
        self.timestamp = None
        self.translation = None
        self.rotation = None
        self.colorImage = None
        self.depthImage = None
        self.feelings = None

    @staticmethod
    def from_pb_object(self, pb_object):
        self.timestamp = pb_object.timestamp()
        self.translation = 'a'
