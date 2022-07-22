from problem_8.exceptions import *
import os


def validate_unique_sn(func):
    def decorator(*args, **kwargs):
        if args[1] not in IotDevice.devices_list:
            return func(*args, **kwargs)
        else:
            raise DuplicateDeviceException(f"Device with sn '{args[1]}' already exists.")

    return decorator


def validate_environment_variable(func):
    def decorator(*args, **kwargs):
        if args[0] in os.environ:
            return func(*args, **kwargs)
        else:
            raise EnvironmentVariableException(f"Variable '{args[0]}' doesn't exist on you system.")

    return decorator


class IotDevice:
    devices_list = dict()

    @validate_unique_sn
    def __init__(self, sn: int, id: int):
        self.sn = sn
        self.id = id

        if len(IotDevice.devices_list) == 0:
            IotDevice.devices_list = {sn: id}
        else:
            IotDevice.devices_list[sn] = id

    def __str__(self):
        return f"{self.sn},{self.id}"

    @staticmethod
    @validate_environment_variable
    def read(environment_variable: str):
        import csv
        filename = os.environ[environment_variable]

        if not os.path.exists(filename):
            raise FileIsMissingException(f"File '{filename}' doesn't exist.")

        devices = dict()
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                if len(row):
                    if len(devices) == 0:
                        devices = {row[0]: row[1]}
                    elif devices and row[0] not in devices:
                        devices.update({row[0]: row[1]})
                    # Duplicate entries from csv file will be ignored.

        IotDevice.devices_list = devices
        return True

    @staticmethod
    @validate_environment_variable
    def write(environment_variable):
        """
        Flushes all the data stored to a csv file.
        """
        import csv
        filename = os.environ[environment_variable]

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, value in IotDevice.devices_list.items():
                writer.writerow([key, value])

        return True
