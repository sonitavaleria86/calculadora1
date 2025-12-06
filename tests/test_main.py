# test_main_simple.py

from src.operaciones import suma, resta, multiplicacion, division, potencia, modulo, raiz

def test_operacion_suma():
    # Suma
    assert suma(3, 2) == 5
def test_operacion_resta():
    # Resta
    assert resta(5, 1) == 4
def test_operacion_multiplicacion():
    # Multiplicación
    assert multiplicacion(2, 4) == 8
def test_operacion_division():
    # División
    assert division(10, 2) == 5
def test_operacion_potencia():
    # Potencia
    assert potencia(2, 3) == 8
def test_operacion_modulo():
    # Módulo
    assert modulo(10, 3) == 1
def test_operacion_raiz_positiva():
    # Raíz cuadrada positiva
    assert raiz(16) == 4
def test_operacion_raiz_negativa():
    # Raíz cuadrada negativa
    assert raiz(-4) == "Error: No se puede calcular la raiz cuadrada de un numero negativo"