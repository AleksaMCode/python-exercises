# define user-defined exceptions

class EmailException(BaseException):
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


class PasswordFetchException(BaseException):
    def __init__(self, message):
        self.message = message


class EmptyCsvFileException(BaseException):
    def __init__(self, message):
        self.message = message
