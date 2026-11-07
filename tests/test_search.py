import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class SearchTest(unittest.TestCase):
    def test_search_by_category_returns_only_matching_dvds(self):
        lion = DigitalVideoDisc("The Lion King", category="Animation")
        star_wars = DigitalVideoDisc("Star Wars", category="Science Fiction")

        self.assertEqual(
            search_by_category([lion, star_wars], "Animation"),
            [lion],
        )