from calc.sum_of_multiples import sum_of_multiples

def test_sum():
#3 5 6 9 10
    result = sum_of_multiples(10)

    assert result == 33

def test_sum2():

# 3 5 6 9 10 12 15 18 20
    result = sum_of_multiples(20)

    assert result == 98