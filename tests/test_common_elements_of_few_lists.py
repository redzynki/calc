from calc.common_elements_of_few_lists import common_elements

def test_common_elements_1():

    result = common_elements([[1,2,3,3,7,11,1,11],
                              [2,5,7,11,13,15,20],
                              [1,1,2,3,4,4,7,8,11]])
    assert result == [2,7,11]

def test_common_elements_2():
    result = common_elements([[1], [2]])
    assert result == []

def test_common_elements_3():
    result = common_elements([[1,2,3], [1,3], [1,4]])
    assert result == [1]

def test_common_elements_4():
    result = common_elements([[2,2,5,7,8], [2,5,8],[2,5]])
    assert result == [2,5]