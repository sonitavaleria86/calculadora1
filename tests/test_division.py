from src.operaciones import division

def test_division_normal():
    # Caso de la division normal
    assert division(10, 2) == 5
    assert division(45,5) == 9

def test_division_decorador():
    # Como 2 < 8 → se intercambian → division(8, 2) = 4,  decorador: @smart_div
    assert division(2, 8) == 4
    assert division(1, 5) == 5

def test_division_por_cero():
    # Regresa un string de error en terminal
    assert division(40, 0) == "Error: NO existe division entre 0"