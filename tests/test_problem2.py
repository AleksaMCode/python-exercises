import csv

import pytest
from problem_2 import problem2
from problem_2.exceptions import InvalidNumberOfFibonacciNumbers


def read_test_data_from_csv():
    collection = []
    with open("fibonacci_values.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter="\n")
        for row in data:
            collection.append(row[0])
    return collection


@pytest.mark.parametrize("value", [-5, -5.0, 0, 2_000])
def test_fibonacci_exception(value):
    try:
        _ = problem2.fibonacci(value)
    except InvalidNumberOfFibonacciNumbers as e:
        assert type(e) != InvalidNumberOfFibonacciNumbers


def test_fibonacci():
    fib_numbers = read_test_data_from_csv()
    for fib, j in zip(problem2.fibonacci(1_000), range(1000)):
        assert fib == int(fib_numbers[j])
