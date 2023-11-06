# NAMING CONVENTIONS
# files: pytest automatically searches for test files (file that begin with test*) in dir/sub-dir and run
# functions: def test_<name>()
# classes: Test<name>.py
def test_a1():
    # assert keyword: tests if a condition returns True
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a2():
    assert 9/5 == 1.5, "failed test intentionally"
    
def test_a3():
    assert 9//5 == 1  # integer truncating division
    