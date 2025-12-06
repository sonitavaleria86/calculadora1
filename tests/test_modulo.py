from src.operaciones import modulo

def test_modulo_basico():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0
    assert modulo(0, 5) == 0

def test_modulo_negativos():
    assert modulo(-10, 3) == -10 % 3
    assert modulo(10, -3) == 10 % -3

def test_modulo_divisor_cero():
    try:
        modulo(10, 0)
    except ValueError as e:
        if str(e) == "No existe el modulo con un divisor de valor cero.":
            print("Correcto.")
        else:
            print(f"Fallo: {e}")
