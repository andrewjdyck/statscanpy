from unittest import TestCase

import statscanpy as sc

class TestSearch(TestCase):
    def test_search_returns(self):
        search = sc.DataSearch('14100287')
        print(search)
        