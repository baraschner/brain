import gzip
import struct

from brain.utils import Snapshot


class ProtobufReader:
    def __init__(self, file):
        self.file = file
        self.pos = 0

    def read_object(self, message):
        with gzip.open(self.file, 'rb') as f:
            f.seek(self.pos)
            size = struct.unpack("I", f.read(4))[0]
            message.ParseFromString(f.read(size))
            self.pos = f.tell()
        return message

    def __iter__(self):
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
                yield message
