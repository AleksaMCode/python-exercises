import unittest
import os
from hamcrest import assert_that, equal_to
from problem_8.exceptions import *
from problem_8.problem8 import IotDevice
from parameterized import parameterized

unittest.TestLoader.sortTestMethodsUsing = None


class TestIotDevice(unittest.TestCase):
    environment_variable_name = "DEVICES_PATH"
    environment_variable_value = "devices.csv"
    devices_test_data = [
        [213, 121],
        [123, 152],
        [132131, 12],
        [12321, 1211],
        [1232, 85],
        [2134, 75],
        [12414, 347],
    ]

    @classmethod
    def setUpClass(cls):
        os.environ[TestIotDevice.environment_variable_name] = TestIotDevice.environment_variable_value

    @classmethod
    def tearDownClass(cls):
        del os.environ[TestIotDevice.environment_variable_name]

    def test1_0(self):
        """
        Test if the Exception is raised when trying to read from an empty CSV file.
        :return:
        """
        with open(TestIotDevice.environment_variable_value, 'w'):
            pass

        with self.assertRaises(EmptyCsvFileException):
            _ = IotDevice.read(TestIotDevice.environment_variable_name)

    @parameterized.expand(devices_test_data)
    def test1_1(self, sn, id):
        """
        Tests if it's possible to create devices from a list of correct data.
        """
        _ = IotDevice(sn, id)

    def test1_2(self):
        """
        Tests if it's possible to write devices to a csv.
        """
        assert_that(IotDevice.write(TestIotDevice.environment_variable_name), equal_to(True))

    def test1_3(self):
        """
        Tests if it's possible to read devices from a csv.
        """
        assert_that(IotDevice.read(TestIotDevice.environment_variable_name), equal_to(True))

    def test1_4(self):
        """
        Tests if it's possible to read a file when environment variable is missing.
        """
        with self.assertRaises(EnvironmentVariableException):
            _ = IotDevice.read("DEVICES__PATH")

    def test1_5(self):
        """
        Test if it's possible to add device with an already existing sn.
        """
        with self.assertRaises(DuplicateDeviceException):
            _ = IotDevice(TestIotDevice.devices_test_data[0][0], TestIotDevice.devices_test_data[0][1])


if __name__ == '__main__':
    unittest.main()
