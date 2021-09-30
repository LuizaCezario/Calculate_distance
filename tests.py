from blueprint import calculate_distance, api, validate_coordinates
from nose.tools import assert_true
import unittest
import requests

class TestCalculateRoute(unittest.TestCase):
    def test_coordinates(self):
        self.assertAlmostEqual(calculate_distance('50,50'),1048.4448699320176)
        print('ok1')
    def test_out_of_boundary_coordinates(self):
        self.assertEqual(calculate_distance('500,500'),'Latitude must be in the [-90; 90] range and Longitude must be in the [-180; 180] range.')
        print('ok2')
    def test_out_of_boundary_coordinates(self):
        self.assertEqual(calculate_distance('aaaa'),'Latitude must be in the [-90; 90] range and Longitude must be in the [-180; 180] range.')
        print('ok2')
    def test_MKAD_coordinates(self):
        self.assertEqual(calculate_distance('37.841217,55.739103'), 'The coordinates are inside MKAD')
        print('ok3')
    def test_right_coordinates(self):
        self.assertEqual(validate_coordinates('37.841217,55.739103'), True)
        print('ok4')
    def test_validate_wrong_coordinates(self):
        self.assertEqual(validate_coordinates('500,500'), False)
        print('ok5')
    def test_url_get(self):
        response = requests.get('http://127.0.0.1:5000/api/')
        assert_true(response.ok)
        print('ok7')