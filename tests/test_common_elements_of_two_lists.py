from calc.common_elements_of_two_lists import common_elements

def test_common_elements():

    result = common_elements("1,1,2,3,5,8,13,21,34,55,89,1,2,3,4,5,6,7,8,9,10,11,12,13")

    assert result == [1, 2, 3, 5, 8, 13]