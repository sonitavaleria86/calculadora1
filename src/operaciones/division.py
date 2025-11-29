'''Funcion para division dos numeros'''

def smart_div(func):
    def inner(a,b):
         print("Entrando al decorador")
         if a < b:
              a, b = b, a
         return func(a,b)
    return inner   

'''Invocacion del decorador para la division'''
@smart_div
def division(a:float,b:float) -> float:
    '''Devuelve la division de dos numeros
    a: Primer numero
    b: Segundo numero
    Returns:
    Devuelve resultado de la division de dos numeros a/b si b es 0, retorna un Error.  
    '''
    if b==0 : 
                return "Error: NO existe division entre 0"
    '''Devuelve error en caso de que el segundo numero sea igual a 0'''
    return a/b 