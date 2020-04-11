import json


class MessageBase:
    def to_json(self):
        return json.dumps(self.__dict__)
