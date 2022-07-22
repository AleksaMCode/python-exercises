# define user-defined exceptions

class EmailDuplicateException(BaseException):
    def __init__(self, message):
        self.message = message


class InvalidEmailException(BaseException):
    def __init__(self, message):
        self.message = message


class WrongPasswordException(BaseException):
    def __init__(self, message):
        self.message = message


class FileIsMissingException(BaseException):
    def __init__(self, message):
        self.message = message
