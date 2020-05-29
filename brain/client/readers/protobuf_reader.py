import gzip
import struct

from google.protobuf.json_format import MessageToDict

from brain.utils import Snapshot
from brain.utils import User, consts


class ProtobufReader:
    def __init__(self, file):
        self.file = file
        self.pos = 0
        self.supported_fields = [consts.DATETIME]

    def set_supported_fields(self, supported_fields):
        self.supported_fields += supported_fields

    def read_user(self):
        """
        Reads a user object and returns a dict containing the user's information
        :return:
        """
        user = self.__read_object(User())
        user_dict = MessageToDict(user, including_default_value_fields=True)
        user_dict[consts.USER_ID] = int(user_dict[consts.USER_ID])  # protobuf doesn't preserve int64
        return user_dict

    def __read_object(self, message):
        with gzip.open(self.file, 'rb') as f:
            f.seek(self.pos)
            size = struct.unpack("I", f.read(4))[0]
            message.ParseFromString(f.read(size))
            self.pos = f.tell()
        return message

    def __iter__(self):
        """
        Allows iteration over all snapshot.
        Each snapshot is a dict containing the supported fields
        :return:
        """
        with gzip.open(self.file, 'rb') as f:
            while True:
                f.seek(self.pos)
                message = Snapshot()
                size = f.read(4)
                if not size:
                    break
                size = struct.unpack("I", size)[0]
                message.ParseFromString(f.read(size))
                self.pos = f.tell()

                snapshot_dict = MessageToDict(message, including_default_value_fields=True)
                snapshot_dict[consts.DATETIME] = int(snapshot_dict[consts.DATETIME])
                filtered = {key: snapshot_dict[key] for key in self.supported_fields if key in snapshot_dict}
                yield filtered
