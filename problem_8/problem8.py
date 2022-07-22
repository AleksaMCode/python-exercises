from functools import wraps


def decorator_function(num):

        def inner_func(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                result = result + num
                return result

            return wrapper

        return inner_func


class Device:
    devices_list = []

    def __init__(self, sn, id):
        self.sn = sn
        self.id = id

    def __str__(self):
        return f"{self.sn},{self.id}"

    def write(self):
        import csv
        import os
        devices_path = os.environ['DEVICES_PATH']
        with open(devices_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.__str__())

    @staticmethod
    def read():
        import csv
        import os
        devices_path = os.environ['DEVICES_PATH']
        with open(devices_path, 'r') as file:
            devices = csv.reader(file)
            for device in devices:
                device_split = device.strip().split(',')
                Device.devices_list.append(Device(device_split[0], Device(device_split[1]))

    @staticmethod
    @decorator_function(5)
    def function_to(sn):
