# define user-defined exceptions

class DuplicateDeviceException(BaseException):
    def __init__(self, message):
        self.message = message


class FileIsMissingException(BaseException):
    def __init__(self, message):
        self.message = message


class EnvironmentVariableException(BaseException):
    def __init__(self, message):
        self.message = message

class EmptyCsvFileException(BaseException):
    def __init__(self, message):
        self.message = message
