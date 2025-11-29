'''Funcion para obtener el modulo de un numero'''

def modulo(a: float, b: float) -> float:
    """
    Calcula el residuo de la división entre dos números a % b
    a: Dividendo.
    b: Divisor.
    Returns:
    Devuelve el resultado del modulo (residuo de una division) de un numero.
    """
    if b == 0:
        raise ValueError("No existe el modulo con un divisor de valor cero.")
    return a % b