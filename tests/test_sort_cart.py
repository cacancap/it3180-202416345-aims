import unittest
from contextlib import redirect_stdout
from io import StringIO

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartSortTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        with redirect_stdout(StringIO()):
            self.cart.add_dvd(DigitalVideoDisc("Zebra", cost=10.0))
            self.cart.add_dvd(DigitalVideoDisc("Alpha", cost=20.0))
            self.cart.add_dvd(DigitalVideoDisc("Delta", cost=5.0))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in self.cart.items], ["Alpha", "Delta", "Zebra"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in self.cart.items], [5.0, 10.0, 20.0])
