"""
Fixture: functions that are run by pytest before (and sometimes after) actual test functions

Concepts:
- can put fixtures in individual test files or in conftest.py for making fixtures available in multiple tests files
- fixtures function in same test-file/module
- 2 ways to use fixtures
- returning data from fixtures
"""
import pytest

@pytest.mark.parametrize("test_input", [82, 78, 44, 77])
def test_param01(test_input):
    assert test_input > 50