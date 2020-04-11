from brain.protocol.message_base import MessageBase


class HelloRequest(MessageBase):
    def __init__(self, userid, username, birthday, gender):
        self.userid = userid
        self.username = username
        self.birthday = birthday
        self.gender = gender

    @staticmethod
    def from_user(user):
        return HelloRequest(user.user_id, user.username, user.birthday, user.gender)
