import unittest
from models.manufacturer import Manufacturer


class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer_1 = Manufacturer("Bugatti", "France", True)
        self.manufacturer_2 = Manufacturer("Ferrari", "Italy", False)
        self.manufacturers = [self.manufacturer_1, self.manufacturer_2]

    def test_set_operating_status_false(self):
        self.manufacturer_1.set_operating_status_false()
        self.assertEqual(False, self.manufacturer_1.operating_status)

    def test_set_operating_status_true(self):
        self.manufacturer_2.set_operating_status_true()
        self.assertEqual(True, self.manufacturer_2.operating_status)
