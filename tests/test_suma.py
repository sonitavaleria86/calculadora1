from src.operaciones import suma

def test_sumar():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0
    assert suma(30, 10) == 40

def test_sumar_decimales():
    assert suma(17.45, 20) == 37.45
    assert suma(20.15, 10) == 30.15