import datetime


class Members:
    def __init__(self, name, age):
        self. name = name
        self.age = age
        self.iD = None
        self.rent = None
        self.date = datetime.datetime.now()

    def idGenerator(self):
        pass

    def expireCheck(self):
        pass
