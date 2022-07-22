import base64
import re
import os
from passlib.context import CryptContext

from problem_12.exceptions import *


def validate_uniqe_email_decorator(func):
    def inner(*args, **kwargs):
        if len(UserIot.user_dict) == 0:
            UserIot.user_dict = {args[0]: [args[1], args[2]]}
            return func(*args, **kwargs)
        elif UserIot.user_dict and args[0] not in UserIot.user_dict or len(UserIot.user_dict) == 0:
            return func(*args, **kwargs)
        else:
            raise EmailDuplicateException(f"User with '{email}' already exists.")

    return inner


def validate_file_decorator(func):
    def inner(*args, **kwargs):
        if os.path.exists(args[0]):
            return func(*args, **kwargs)
        else:
            raise FileIsMissingException(f"File {args[0]} doesn't exist.")

    return inner


def validate_password_decorator(func):
    def inner(*args, **kwargs):
        if UserIot.digest.verify(args[0], args[1]):
            return func(*args, **kwargs)
        else:
            raise WrongPasswordException("Entered passwords doesn't match the existing password.")

    return inner


def validate_email_decorator(func):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    def inner(*args, **kwargs):
        email_str = args[0]
        if re.search(regex, email_str):
            return func(*args, **kwargs)
        else:
            raise InvalidEmailException(f"Email {email_str} is invalid.")

    return inner


def update_csv(users):
    import csv
    import os
    path = "users.csv"
    os.remove(path)
    with open(path, 'a', newline='') as f:
        for key in users.keys():
            writer = csv.writer(f)
            writer.writerow([key, users[key][0], users[key][1]])


class UserIot:
    user_dict = dict()
    digest = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @validate_email_decorator
    @validate_uniqe_email_decorator
    def __init__(self, email: str, password: str, rol: int):
        self.email = email
        self.password = base64.b64encode(UserIot.hash_the_password(password).encode('utf-8'))
        self.rol = rol

    @staticmethod
    @validate_email_decorator
    def update_user(email: str, password: str, rol: int):
        """
        Updates existing user by using email as a key value.
        :param email:
        :param password:
        :return:
        """
        if UserIot.user_dict and len(UserIot.user_dict) != 0 and email in UserIot.user_dict:
            UserIot.user_dict[email] = [password, rol]
        else:
            raise EmailDuplicateException(f"User with '{email}' doesn't exists.")

    @staticmethod
    @validate_file_decorator
    def read(filename: str):
        """
        Loads all the users from the csv file.
        :param filename: Name of the csv file.
        """
        import csv

        users = dict()
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                if len(row):
                    if len(users) == 0:
                        users = {row[0]: [row[1], row[2]]}
                    elif users and row[0] not in users:
                        users.update({row[0]: [row[1], row[2]]})
                    # Duplicate entries from csv file will be ignored.

        UserIot.user_dict = users
        return True

    @staticmethod
    def write(filename: str):
        """
        Flushes all the data stored on the users to a csv file.
        :param filename: Name of the csv file.
        :return:
        """
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, value in UserIot.user_dict.items():
                writer.writerow([key, value[0], value[1]])

        return True

    @staticmethod
    @validate_password_decorator
    def login_simulation(plain_password: str, hashed_password: str):
        return "Success!"


# if __name__ == '__main__':
#     n = -1
#
#     while n < 0:
#         n = int(input("Enter number of Users: "))
#
#     i = 0
#     while i < n:
#         try:
#             print(f"User {i + 1}")
#             email = str(input("Enter Email: "))
#             password = str(input("Enter Password: "))
#             rol = int(input("Enter rol: "))
#             user = UserIot(email, password, rol)
#             user.write()
#             i += 1
#         except Exception as e:
#             print(e)
#
#     n = -1
#
#     while n < 0:
#         n = int(input("Enter number of Users for update: "))
#
#     users = UserIot.read()
#     i = 0
#     while i < n:
#         try:
#             email = str(input("Enter Email: "))
#             validate_email(email)
#             password = str(input("Enter Password: "))
#             rol = int(input("Enter rol: "))
#
#             if email in users:
#                 users.update({email: [base64.b64encode(UserIot.hash_the_password(password).encode('utf-8')), rol]})
#             else:
#                 print(f"Email {email} doesn't exist.")
#
#             i += 1
#         except Exception as e:
#             print(e)
#
# update_csv(users)
#
# print("Let's match user and password:")
# while True:
#     email = str(input("Enter Email: "))
#     password = str(input("Enter Password: "))
#
#     try:
#         validate_email(email)
#         if email in users:
#             UserIot.validate_password(password, base64.b64decode(users[email][0]))
#             print("Passwords match.")
#         else:
#             print(f"Email {email} doesn't exist.")
#     except Exception as e:
#         print(e)
