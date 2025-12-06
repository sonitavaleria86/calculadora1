import math
from src.operaciones import raiz 

def test_raiz_num_positivos():
    assert raiz(4) == 2
    assert raiz(9) == 3
    assert raiz(0) == 0

def test_raiz_num_negativos():
    assert raiz(-1) == "Error: No se puede calcular la raiz cuadrada de un numero negativo"
    assert raiz(-100) == "Error: No se puede calcular la raiz cuadrada de un numero negativo"

def test_raiz_decimales():
    # Números decimales positivos
    assert math.isclose(raiz(2.25), 1.5, rel_tol=1e-9)
    assert math.isclose(raiz(0.01), 0.1, rel_tol=1e-9)
    assert math.isclose(raiz(0.5), math.sqrt(0.5), rel_tol=1e-9)