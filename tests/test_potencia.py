from src.operaciones import potencia


def test_potencia_num_positivos():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(0, 5) == 0

def test_potencia_num_negativos():
    assert potencia(-2, 3) == -8
    assert potencia(-2, 2) == 4
