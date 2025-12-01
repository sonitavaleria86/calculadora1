'''Módulo de operación de división de dos numeros con uso de decoradores'''

def smart_div(func):
     '''Decorador para funciones de division: Este decorador verifica si el primer número (a) es menor que el 
     segundo (b). Si es así, intercambia los valores antes de ejecutar la función decorada. Sirve para asegurar que la 
     división se realice con un numerador mayor, evitando resultados decimales inesperados'''
     def inner(a,b):
          print("Entrando al decorador")
          #Intercambiamos valores si el numerador es menor
          if a < b:
               a, b = b, a
          return func(a,b)
     return inner   

'''Invocacion del decorador para la division'''
@smart_div
def division(a:float,b:float) -> float:
     '''Devuelve la division de dos números.

     Esta función realiza la operación a/b y contempla el caso de la división entre cero, en cuyo caso retorna un 
     mensaje de error.

     Parámetros:
     a (float): Primer número (numerador)
     b (float): Segundo número (denominador)

     Returns:
     float / str: Devuelve resultado de la division de dos numeros a/b si b es 0, retorna un Error.'''
     #Verificación de división entre cero
     if b==0 : 
          return "Error: NO existe division entre 0"
     '''Devuelve error en caso de que el segundo numero sea igual a 0'''
     return a/b 