def validate_unique_sn_decorator(func):
    def inner(*args, **kwargs):
        if args[1] not in IotDevice.devices_list:
            return func(*args, **kwargs)
        else:
            raise Exception(f"Device with sn '{args[1]}' already exists.")

    return inner


class IotDevice:
    devices_list = dict()

    @validate_unique_sn_decorator
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
    def read():
        import csv
        import os
        filename = os.environ['DEVICES_PATH']

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
    def write():
        """
        Flushes all the data stored to a csv file.
        """
        import csv
        import os
        filename = os.environ['DEVICES_PATH']

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, value in IotDevice.devices_list.items():
                writer.writerow([key, value])

        return True
