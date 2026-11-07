import unittest
from contextlib import redirect_stdout
from io import StringIO

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartTest(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        with redirect_stdout(StringIO()):
            for number in range(1, 21):
                self.assertTrue(
                    cart.add_dvd(DigitalVideoDisc(f"DVD {number}")),
                    f"DVD {number} should be accepted",
                )

            added = cart.add_dvd(DigitalVideoDisc("DVD 21"))

        self.assertFalse(added, "The 21st DVD should be rejected")
        self.assertEqual(len(cart.items), 20)
