import csv

from problem_2 import problem2


def read_test_data_from_csv():
    test_data = []
    with open("fibonacci_values.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter="\n")
        for row in data:
            test_data.append(int(row[0], 10))
    return test_data


if __name__ == '__main__':
    value = read_test_data_from_csv()
    fib_value = problem2.fibonacci(1000)
    for i in range(1000):
        print(f"{i + 1} Fibonacci element match: {value[i] == next(fib_value)}")

    print()
    fib_value = problem2.fibonacci_recursive()
    for i in range(900):
        print(f"{i + 1} Fibonacci element match: {value[i] == next(fib_value)}")

