from src.operaciones import multiplicacion

def test_multiplicar():
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(10, 10) == 100

def test_multiplicar_decimales():
    assert multiplicacion(15.72, 4) == 62.88

def test_multiplicar_0():
    assert multiplicacion(1, 0) == 0