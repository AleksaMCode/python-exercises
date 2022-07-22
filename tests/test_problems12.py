import unittest

from problem_12.exceptions import *
from problem_12.problem12 import UserIot
from parameterized import parameterized

unittest.TestLoader.sortTestMethodsUsing = None


class TestUserIot(unittest.TestCase):
    users_test_data = [
        ["user1@gmail.com", "lozinka1", 121],
        ["user2@gmail.com", "lozinka2", 152],
        ["user3@gmail.com", "lozinka3", 12],
        ["user4@gmail.com", "lozinka4", 1211],
        ["user5@gmail.com", "lozinka5", 85],
        ["user6@gmail.com", "lozinka6", 75],
        ["user7@gmail.com", "lozinka7", 347],
    ]

    @parameterized.expand(users_test_data)
    def test1(self, email, password, rol):
        _ = UserIot(email, password, rol)

    def test2(self):
        self.assertEqual(True, UserIot.write("users.csv"))

    def test3(self):
        self.assertEqual(True, UserIot.read("users.csv"))

    def test4(self):
        with self.assertRaises(FileIsMissingException):
            _ = UserIot.read("user.csv")

    def test5(self):
        with self.assertRaises(EmailDuplicateException):
            _ = UserIot("user1@gmail.com", "lozinka1", 121)
