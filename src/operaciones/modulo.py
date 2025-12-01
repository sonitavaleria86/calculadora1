'''Módulo con la Funciónn para obtener el módulo de un número. 
Este archivo contiene la función módulo que calcula el residuo de dividr un número entre otro y maneja errores
asociados al divisor cero'''

def modulo(a: float, b: float) -> float:
    """
    Calcula el residuo (módulo= de la división entre dos números a % b
    El módulo representa el residuo entero o decimal que resulta después de dividir a entre b. 
    
    Parámetro:
    a (float): Dividendo: Número al cual se le aplicará la operación módulo
    b (float): Divisor: Número por el cual se dividirá a
    
    Returns:
    float: el reiduo de la operación a/b
    Devuelve el resultado del modulo (residuo de una division) de un numero.
    Value Error: si el divisor b es igual a cero, ya que el módulo con divisor cero no está definido matemáticamente
    """
    if b == 0:
        raise ValueError("No existe el modulo con un divisor de valor cero.")
    return a % b