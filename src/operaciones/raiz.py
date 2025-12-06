import math

def raiz(a: float) -> float:
    """
    Devuelve la raiz cuadrada de un numero positivo.

    Parametros:
    a (float): Numero al que se le quiere calcular la raiz cuadrada

    Returns:
    float: Raiz cuadrada de 'a'
    str: Mensaje de error si 'a' es negativo
    """
    if a < 0:
        return "Error: No se puede calcular la raiz cuadrada de un numero negativo"
    return math.sqrt(a)