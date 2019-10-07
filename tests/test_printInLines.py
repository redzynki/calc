from calc.printInLines import inLines

def test_inLines():

    result = inLines([1,2,3,4,5])

    assert result == ("1\n2\n3\n4\n5")

