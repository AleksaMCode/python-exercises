from problem_2.exceptions import InvalidNumberOfFibonacciNumbers


# def fibonacci_recursive(start=0, next_val=1):
#     """
#     Generator recursive function that calculates next number in Fibonacci sequence.
#     :param start: First value of Fibonacci sequence
#     :param next_val: Second value of Fibonacci sequence
#     :return: Next number in Fibonacci sequence.
#     """
#     # This will error out once the maximum recursion depth is reached. Not the best solution.
#     yield start
#     yield from fibonacci_recursive(next_val, start + next_val)


def fibonacci(n: int) -> int:
    """
    Generator function that calculates n number in Fibonacci sequence.
    :param n: Total number of Fibonacci sequence elements
    :return: First n Fibonacci numbers
    """
    if n <= 0:
        raise InvalidNumberOfFibonacciNumbers(f"{n} isn't a valid number of Fibonacci numbers.")
    elif n > 1_000:
        raise InvalidNumberOfFibonacciNumbers(f"{n} isn't a valid number of Fibonacci numbers. Upper limit is set to "
                                              f"1,000 elements.")

    start, next_val = 0, 1
    for _ in range(n):
        yield start
        next_val, start = start, start + next_val  # Tuple swap
    return
