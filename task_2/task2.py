import time


def fibonacci_recursive(start=0, next_val=1):
    """
    Generator function that calculates next number in Fibonacci sequence using recursion.
    :param start: First value of Fibonacci sequence
    :param next_val: Second value of Fibonacci sequence
    :return: Next number in Fibonacci sequence.
    """
    # This will error out once the maximum recursion depth is reached. Not the best solution.
    yield start + next_val
    yield from fibonacci_recursive(next_val, start + next_val)
