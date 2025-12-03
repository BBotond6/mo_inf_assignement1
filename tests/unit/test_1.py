from src.test_class import test_class

def test_is_numeric():
    test_var = test_class()

    assert test_var.is_numeric("1")    == True
    assert test_var.is_numeric("123e") == False

def test_less_than_10():
    test_var = test_class()

    assert test_var.less_than_10(1)  == True
    assert test_var.less_than_10(10) == False
