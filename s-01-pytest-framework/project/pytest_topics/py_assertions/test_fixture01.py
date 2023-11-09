"""
fixtures used to initialize connections or open files
"""
import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ["Los Angeles", "Greenville", "Manila", "New York", "Mumbai"]
    return city

def test_getItem(setup_list):
    print(setup_list)
    assert setup_list[0] == "Los Angeles"
    assert setup_list[::2] == ["Los Angeles", "Manila", "Mumbai"]

def myReverse(my_list):
    my_list.reverse()
    return my_list

def test_reverseList(setup_list):
    assert setup_list[::-2] == ["Mumbai", "Manila", "Los Angeles"]
    assert setup_list[::-1] == myReverse(setup_list)