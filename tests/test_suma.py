from src.operaciones import suma

def test_sumar():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0
    assert suma(30, 10) == 40
    assert suma(17.45, 20) == 37.45