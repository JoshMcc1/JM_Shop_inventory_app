import unittest
from models.product import Product
from models.manufacturer import Manufacturer


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.manufacturer_1 = Manufacturer("Bugatti", "France", True)
        self.product_1 = Product(
            "Veyron",
            "TThe development of the BUGATTI VEYRON was one of the greatest technological challenges ever known in the automotive industry.",
            10,
            400000.00,
            1200000.00,
            self.manufacturer_1,
            1000,
            260,
            "Car",
        )

    def test_calculate_makrup(self):
        self.assertEqual(800000.00, self.product_1.calculate_markup())
