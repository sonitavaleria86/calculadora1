from src.operaciones import resta

def test_restar():
    assert resta(5, 3) == 2
    assert resta(10, 5) == 5
    assert resta(350, 10) == 340

def test_restar_decimales():
    assert resta(45.2, 10) == 35.2
    assert resta(45.2, 10.1) == 45.2-10.1