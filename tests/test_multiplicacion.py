from src.operaciones import multiplicacion

def test_multiplicar():
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(10, 10) == 100
    assert multiplicacion(15.72, 4) == 62.88
    assert multiplicacion(1, 0) == 0