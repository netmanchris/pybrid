from unittest import TestCase
from pybridair.auth import *
from pybridair.device import *
import vcr

my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='./test_pyhpecfm/fixtures/cassettes',
    record_mode='new_episodes',
    match_on=['uri', 'method'],
)

auth = BridAuth('10.101.30.42')

class TestGetDeviceInfo(TestCase):
    """
    Test pybrid.data.get_status function against live Brid device
    """
    @vcr.use_cassette(cassette_library_dir='./tests/fixtures/cassettes')
    def test_get_device_info(self):
        """
        Tests pybrid.data.get_device_info function against live Brid device
        """
        dev_status = get_device_info(auth)
        data_points = ['Model', 'Serial Number', 'Manufacturer', 'Version']
        for data_point in dev_status.keys():
            self.assertIn(data_point, data_points)

class TestSetDeviceMode(TestCase):
    """
    Test pybrid.data.get_status function against live Brid device
    """

    @vcr.use_cassette(cassette_library_dir='./tests/fixtures/cassettes')
    def test_set_device_mode(self):
        """
        Tests pybrid.data.get_history function against live Brid device
        """
        modes = {
            "off": 0,
            'smart': 1,
            'auto': 2,
            'boost': 3,
            'night': 4
        }
        for mode in modes:
            desired_mode = set_device_mode(auth, mode)
            self.assertIn('success', desired_mode.keys())
            self.assertIs(desired_mode['success'], 0)





{"off" : 0,
             'smart' : 1,
             'auto' : 2,
             'boost' : 3,
             'night' : 4}