from src.test_class import test_class

def test_functionality1():
    test_var = test_class()

    test_value = "1"

    if test_var.is_numeric(test_value):
        assert test_var.less_than_10(test_value) == True
        assert test_var.is_div_by_2(test_value)  == False
    
    test_value = "126"

    if test_var.is_numeric(test_value):
        assert test_var.less_than_10(test_value) == False
        assert test_var.is_div_by_2(test_value)  == True
    
    test_value = "2f"

    assert test_var.is_numeric(test_value) == False
