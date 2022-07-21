# define user-defined exceptions

class BadArgumentException(BaseException):
    def __init__(self, message):
        self.message = message


class DenominatorZeroException(BaseException):
    def __init__(self, message):
        self.message = message
