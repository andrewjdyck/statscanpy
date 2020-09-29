import pytest

def test_api_response():
    assert get_series_update_list().status_code == 200

def test_api_valid_json():
    assert get_series_update_list().json() is dict
