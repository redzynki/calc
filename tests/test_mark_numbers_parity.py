from calc.mark_numbers_parity import numbers_parity

def test_parity():

    result = numbers_parity(6)

    assert result == ("0 EVEN\n1 ODD\n2 EVEN\n3 ODD\n4 EVEN\n5 ODD\n6 EVEN")