"""
Calculadora básica en Python
Funciones: suma, resta, multiplicacion y dividicion para 2 numeros flotantes
Autores: Sonia Valeria Aviles Sacoto, Alexis Nuñez Gonzalez, Jose Benjamin Flores Lopez
"""

'''Funcion para sumar dos numeros'''
def suma(a:float,b:float) -> float:
    '''Devuelve la suma de dos numeros
    a: Primer numero 
    b: Segundo numero 
    Returns:
    Devuelve resultado de la suma de a+b 
        '''
    return a+b 


'''Funcion para restar dos numeros'''
def resta(a:float,b:float) -> float:
    '''Devuelve la resta de dos numeros
    a: Primer numero
    b: Segundo numero
    Returns:
    Devuelve resultado de la resta de a-b  
        '''
    return a-b 

'''Funcion para multiplicar dos numeros'''
def multiplicacion(a:float,b:float) -> float: 
    '''Devuelve la multiplicacion de dos numeros
    a: Primer numero
    b: Segundo numero
    Returns:
    Devuelve resultado de la multiplicacion de dos numeros a*b  
        '''
    return a*b 

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


def menu():
    """
    Muestra menu de opciones al usuario.
    """
    while True:
        print("\n Calculadora de Operaciones Basicas")
        print("Presione 1 si desea realizar una: SUMA")
        print("Presione 2 si desea realizar una: RESTA")
        print("Presione 3 si desea realizar una: MULTIPLICACION")
        print("Presione 4 si desea realizar una: DIVISION")
        print("Presione 5 si desea SALIR del programa")

        '''Solicita al usuario la eleccion de una opcion'''
        opcion = input("Seleccione una opcion del 1 al 5: ")

        '''Si el usuario eligio la opcion 5, el programa se cierra'''
        if opcion == "5":
            print("Saleindo de calculadora...")
            break

            '''Si el usuario elige una opcion diferente a las mostradas en el menu; se imprime un aviso'''
        if opcion not in ["1", "2", "3", "4"]:
            print("\n --AVISO: La opcion seleccionada NO EXISTE:")
            print("Vuelva a intentar con una opcion del 1 al 5--")
            continue

        # El programa captura los valores de a(flotante) y b(flotante) que proporciono el usuario
        try:
            '''El usuario ingresa los valores (a y b)'''
            a = float(input("Ingresa el primer valor: "))
            b = float(input("Ingresa el segundo valor: "))
            '''Si el usuario no ingresa un numero de manera correcta. El programa imprime un aviso'''
        except ValueError:
            print("\n Error: Alguno o algunos de los valores que ingresaste no es valido")
            print("Intenta con un valor de tipo FLOTANTE")
            continue

        # Operaciones 
        '''Si el usuario selecciona la opcion 1, entonces el programa realiza una suma'''

#Si el usuario selecciona la opcion 1, entonces el programa realiza una suma
        if opcion == "1":
            print("Resultado:", suma(a, b))
#Si el usuario selecciona la opcion 2, entonces el programa realiza una resta
        elif opcion == "2":
            print("Resultado:", resta(a, b))
#Si el usuario selecciona la opcion 3, entonces el programa realiza una multiplicacion
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
#Si el usuario selecciona la opcion 4, entonces el programa realiza una division con decorador
        elif opcion == "4":
            print("Resultado:", division(a, b))


# Llamar a la funcion menu
if __name__ == "__main__":
    menu()