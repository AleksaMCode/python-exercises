import csv

import pytest
from problem_3 import problem3


def read_test_data_from_csv():
    test_data = []
    with open("palindromes.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter="\n")
        for row in data:
            test_data.append(row[0])
    return test_data


@pytest.mark.parametrize("palindrome", read_test_data_from_csv())
def test_palindrome_check1(palindrome):
    assert problem3.palindrome_check1(palindrome) is True


# @pytest.mark.dependency(depends=['test_palindrome_check1'])
@pytest.mark.parametrize("palindrome", read_test_data_from_csv())
def test_palindrome_check2(palindrome):
    assert problem3.palindrome_check2(palindrome) is True


@pytest.mark.parametrize("word, result",
                         [("This is a test", False),
                          ("I'm a palindrome", False),
                          ])
def test_palindrome_check(word, result):
    assert problem3.palindrome_check1(word) is result
