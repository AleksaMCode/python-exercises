# define user-defined exceptions

class InvalidQuadraticEqParam(BaseException):
    def __init__(self, message):
        self.message = message