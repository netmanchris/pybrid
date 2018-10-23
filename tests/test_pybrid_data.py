from unittest import TestCase
from pybrid.auth import *
from pybrid.data import *

auth = BridAuth('10.101.0.124')

class TestGetStatus(TestCase):
    """
    Test pybrid.data.get_status function against live Brid device
    """

    def test_get_current_air(self):
        """
        Tests pybrid.data.get_status function against live Brid device
        """
        current_status = get_status(auth)
        data_points = ['Time', 'Sensors', 'Settings', 'Filters']
        for data_point in current_status.keys():
            self.assertIn(data_point, data_points)


class TestGetDeviceInfo(TestCase):
    """
    Test pybrid.data.get_status function against live Brid device
    """

    def test_get_device_info(self):
        """
        Tests pybrid.data.get_device_info function against live Brid device
        """
        dev_status = get_device_info(auth)
        data_points = ['Model', 'Serial Number', 'Manufacturer', 'Version']
        for data_point in dev_status.keys():
            self.assertIn(data_point, data_points)


class TestGetHistory(TestCase):
    """
    Test pybrid.data.get_status function against live Brid device
    """

    def test_get_history(self):
        """
        Tests pybrid.data.get_history function against live Brid device
        """
        history = get_history(auth)
        data_points = ['t', 'V', 'T', 'H', 'C']
        for data_point in history[0].keys():
            self.assertIn(data_point, data_points)