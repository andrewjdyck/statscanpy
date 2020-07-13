import pytest
import statscanpy as sc

def test_census_bad_json():
    bad_json = '//{"bad_json": 1}'
    assert type(sc.Census().clean_bad_json(bad_json)) is dict

def test_census_good_json():
    good_json = '{"good_json": 1}'
    assert type(sc.Census().clean_bad_json(good_json)) is dict
