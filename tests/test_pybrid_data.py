from unittest import TestCase
from pybrid.auth import *
from pybrid.data import *

auth = BridAuth('10.101.0.124')

class TestGetStatus(TestCase):
    """
    Test Case for pyawair.data get_current_air_data function
    """

    def test_get_current_air(self):
        """
        """
        current_status = get_status(auth)
        data_points = ['Time', 'Sensors', 'Settings', 'Filters']
        for data_point in current_status.keys():
            self.assertIn(data_point, data_points)
