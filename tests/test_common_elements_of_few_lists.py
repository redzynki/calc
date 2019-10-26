from calc.common_elements_of_few_lists import common_elements

def test_common_elements():

    result = common_elements("""1,2,3,3,7,11,11,11,2,5,7,11,13,
                15,20,1,2,3,7,11,55,116,1,1,1,2,3,4,4,7,8,11""")

    assert result == [2,7,11]