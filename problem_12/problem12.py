import base64
import hashlib
import re
import os

from problem_12.exceptions import *


def validate_unique_email_decorator(func):
    def inner(*args, **kwargs):
        if args[1] not in UserIot.user_dict:
            return func(*args, **kwargs)
        else:
            raise EmailException(f"User with email '{args[1]}' already exists.")

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
        if UserIot.verify_hash(args[0], args[1]):
            return func(*args, **kwargs)
        else:
            raise WrongPasswordException(f"Entered passwords '{args[0]}' doesn't match the existing password.")

    return inner


def validate_email_decorator(func):
    regex = r'^[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*' \
            r'[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$'

    def inner(*args, **kwargs):
        email_str = args[1]
        if re.search(regex, email_str):
            return func(*args, **kwargs)
        else:
            raise InvalidEmailException(f"Email {email_str} is invalid.")

    return inner


class UserIot:
    user_dict = dict()

    @validate_email_decorator
    @validate_unique_email_decorator
    def __init__(self, email: str, password: str, rol: int):
        self.email = email
        self.password = UserIot.convert_to_base64(UserIot.hash_the_password(password))
        self.rol = rol

        if len(UserIot.user_dict) == 0:
            UserIot.user_dict = {email: [self.password, rol]}
        else:
            UserIot.user_dict[email] = [self.password, rol]

    @staticmethod
    @validate_email_decorator
    def update_user(password: str, email: str, rol: int):
        """
        Updates user information using the email as key.
        :param password: User's new password
        :param email: User's existing email
        :param rol: User's new rol
        """
        if UserIot.user_dict and len(UserIot.user_dict) != 0 and email in UserIot.user_dict:
            UserIot.user_dict[email] = [UserIot.convert_to_base64(UserIot.hash_the_password(password)), rol]
        else:
            raise EmailException(f"User with '{email}' doesn't exists.")

    @staticmethod
    def hash_the_password(password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def convert_to_base64(string):
        return base64.b64encode(string.encode()).decode('ascii').strip()

    @staticmethod
    def verify_hash(plain_password: str, hashed_password: str):
        return UserIot.convert_to_base64(UserIot.hash_the_password(plain_password)) == hashed_password

    @staticmethod
    @validate_file_decorator
    def read(filename: str):
        """
        Reads all the users from the csv file.
        :param filename: Name of the csv file
        :return True if reading was successful, otherwise Exception is raised
        """
        import csv

        if os.stat(filename).st_size == 0:
            raise EmptyCsvFileException(f"File '{filename}' is empty.")

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
        :param filename: Name of the csv file
        :return: True if writing was successful, otherwise Exception is raised
        """
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, value in UserIot.user_dict.items():
                writer.writerow([key, value[0], value[1]])

        return True

    @staticmethod
    def fetch_password_from_email(email: str):
        if len(UserIot.user_dict) == 0:
            raise PasswordFetchException(f"User dictionary is empty.")
        elif email not in UserIot.user_dict:
            raise PasswordFetchException(f"Email '{email} doesn't exist.")
        else:
            return UserIot.user_dict[email][0]

    @staticmethod
    @validate_password_decorator
    def login_simulation(plain_password: str, hashed_password: str):
        return "Success!"
