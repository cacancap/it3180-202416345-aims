import unittest
from contextlib import redirect_stdout
from io import StringIO

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        with redirect_stdout(StringIO()):
            self.cart.add_dvd(DigitalVideoDisc("DVD", cost=100.0))

    def test_returns_total_after_discount(self):
        self.assertAlmostEqual(self.cart.total_cost_with_discount(20), 80.0)

    def test_rejects_percentage_above_100(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)
