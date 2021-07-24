from datetime import datetime


class User:
    id = ""
    name = ""
    # timestamp = datetime()

    def __init__(self):
        pass

    def set_user_name(self, message):
        self.name = message

    # def set_user_timestamp(self, timestamp):
    #     self.timestamp = datetime(timestamp)

    def get_user(self):
        return {'id': self.id, 'name': self.name}
