from brain.parsers import Parser
from brain.utils import consts
'''
class SnapshotMessage():
    def __init__(self, data):
        self.data = data
        self.user_id = data[consts.USER_ID]
        self.timestamp = data[consts.TIMESTAMP]
        self.binary_fields = []


    def handle_snapshot_message(self):
        context = Context.initialize_from_request(self.data)
        for k,v in self.data.items():
            if k in binary_fields:
                parser.Parser(context)
                del self.data[k]
            
'''


