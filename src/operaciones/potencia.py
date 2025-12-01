'''Módulo con la Función para elevar un número a una potencia. Este archivo contiene la función potencia que calcula
la operación a elevado a b utilizando el operador exponencial (**)'''
def potencia(a: float, b: float) -> float:
    '''Devuelve la potencia de un número: a elevado a la b (a ** b).
    Esta función permite calcular exponentes enteros y deciamles, tanto positivos como negativos. 

    Parámetros:
    a (float): Base de la operación. Número que será elevado a la potencia
    b (float): Exponente. Determina cuántas veces se multiplica la base por sí misma, o si se
    realiza una ráiz o una inversión (en caso de exponentes negativos).

    Returns:
    Float: Devuelve resultado de la potencia de un numero: 'a' elevado a la 'b'
        '''
    return a ** b