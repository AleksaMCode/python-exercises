# define user-defined exceptions

class BadArgumentException(BaseException):
    def __init__(self, message):
        self.message = message


class BadCollectionType(BaseException):
    def __init__(self, message):
        self.message = message
