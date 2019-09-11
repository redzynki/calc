from calc.add import add

def test_add():
    num1 = 1
    num2 = 2

    result = add(num1, num2)

    assert result == 3

def test_add_2():
    result = add(15, 11)

    assert result == 26

