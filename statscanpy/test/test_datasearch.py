from unittest import TestCase

import statscanpy

class TestSearch(TestCase):
    def test_search_returns(self):
        search = statscanpy.datasearch('14100287')
        print(search)
        