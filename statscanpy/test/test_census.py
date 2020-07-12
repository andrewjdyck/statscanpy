import statscanpy as sc
import pytest

# Initiate the class
census = sc.Census()

# Get data with default parameters
result = census.get_cpr_geo()
# print(result)

def test_census_cpr():
    assert isinstance(census.get_cpr_geo(), dict)

