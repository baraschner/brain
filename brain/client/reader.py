import gzip

# from brain.utils import pb_objects


class Reader:
    def __init__(self, file):
        self.file = file
        self.pos = 0
        self.snapshots = None
        # self.user = pb_objects.User()
        # self.__read_object(self.user)
        # print(self.user)

    def __read_object(self, obj_to_init):
        obj_to_init.Clear()
        with gzip.open(self.file) as f:
            data = f.read(100)
            obj_to_init.ParseFromString(data)
