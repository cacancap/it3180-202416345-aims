import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTitleCaseTest(unittest.TestCase):
    def test_finds_title_regardless_of_case(self):
        lion = DigitalVideoDisc("The Lion King")
        aladdin = DigitalVideoDisc("Aladdin")

        self.assertEqual(search_by_title([lion, aladdin], "lion"), [lion])
