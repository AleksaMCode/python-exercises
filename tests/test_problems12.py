import unittest

from problem_12.exceptions import *
from problem_12.problem12 import UserIot
from parameterized import parameterized

unittest.TestLoader.sortTestMethodsUsing = None


class TestUserIot(unittest.TestCase):
    filename = "users.csv"
    users_test_data = [
        ["user1@gmail.com", "password1", 121],
        ["user2@gmail.com", "password2", 152],
        ["user3@gmail.com", "password3", 12],
        ["user4@gmail.com", "password4", 1211],
        ["user5@gmail.com", "password5", 85],
        ["user6@gmail.com", "password6", 75],
        ["user7@gmail.com", "password7", 347],
    ]

    email_test_data = [
        "user1@gmail.com", "user2@gmail.com", "user3@gmail.com", "user4@gmail.com", "user5@gmail.com",
        "user6@gmail.com", "user7@gmail.com"
    ]

    @parameterized.expand(email_test_data)
    def test1_0(self, email):
        """
        Tests if fetching with email works if the user dict is empty.
        :param email: Email used to fetch data.
        """
        with self.assertRaises(PasswordFetchException):
            _ = UserIot.fetch_password_from_email(email)

    @parameterized.expand(users_test_data)
    def test1_1(self, email, password, rol):
        """
        Tests if it's possible to create users from a list of correct data.
        :param email: User's email
        :param password: User's password
        :param rol: User's rol value
        """
        _ = UserIot(email, password, rol)

    def test1_2(self):
        """
        Tests if it's possible to write users to a csv.
        """
        self.assertEqual(True, UserIot.write(TestUserIot.filename))

    def test1_3(self):
        """
        Tests if it's possible to read users from a csv.
        """
        self.assertEqual(True, UserIot.read(TestUserIot.filename))

    def test1_4(self):
        """
        Tests if it's possible to read a file that doesn't exist on the file system.
        """
        with self.assertRaises(FileIsMissingException):
            _ = UserIot.read("userss.csv")

    def test1_5(self):
        """
        Test if it's possible to add user with an already existing email address.
        """
        with self.assertRaises(EmailException):
            _ = UserIot(TestUserIot.users_test_data[0][0], TestUserIot.users_test_data[0][1],
                        TestUserIot.users_test_data[0][2])

    @parameterized.expand(email_test_data)
    def test1_6(self, email):
        """
        Tests if fetching with email works.
        :param email: Emails used to fetch data.
        """
        _ = UserIot.fetch_password_from_email(email)

    def test1_7(self):
        """
        Tests fetching with an unknown email.
        """
        with self.assertRaises(PasswordFetchException):
            _ = UserIot.fetch_password_from_email("test@gmail.com")

    @parameterized.expand(users_test_data)
    def test1_8(self, email, password, rol):
        """
        Tests if the simulated login works i.e. if the entered password matches stored hashed password.
        """
        self.assertEqual("Success!", UserIot.login_simulation(password, UserIot.fetch_password_from_email(email)))

    def test1_9(self):
        """
        Tests the simulated login with wrong password.
        """
        with self.assertRaises(WrongPasswordException):
            _ = UserIot.login_simulation("password", UserIot.fetch_password_from_email("user1@gmail.com"))

    def test2_0(self):
        """
        Tests user update.
        """
        UserIot.update_user("new_password", "user1@gmail.com", 334)

    def test2_1(self):
        """
        Tests user update with non-existing email.
        """
        with self.assertRaises(EmailException):
            UserIot.update_user("new_password", "user1000@gmail.com", 334)
