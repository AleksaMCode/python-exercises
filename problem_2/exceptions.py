# define user-defined exceptions

class InvalidNumberOfFibonacciNumbers(BaseException):
    def __init__(self, message):
        self.message = message