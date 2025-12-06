from src.operaciones import division

def test_division_normal():
    assert division(10, 2) == 5
    assert division(45,5) == 9

def test_division_decorador():
    # Como 2 < 8 se intercambian la division(8, 2) = 4,  uso del decorador: @smart_div
    assert division(2, 8) == 4
    assert division(1, 5) == 5

def test_division_por_cero():
    # Regresa la cadena de error.
    assert division(40, 0) == "Error: NO existe division entre 0"