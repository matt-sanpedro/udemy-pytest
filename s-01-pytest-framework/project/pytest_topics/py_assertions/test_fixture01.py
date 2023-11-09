"""
fixtures used to initialize connections or open files
"""
import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ["Los Angeles", "Greenville", "Manila", "New York"]
    return city

def test_getItem(setup_list):
    pass