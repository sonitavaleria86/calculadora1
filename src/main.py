'''Archivo principal de la calculadora. 

Este módulo implementa un menú interactivo que permite al usuario seleccionar distintas operaciones aritméticas básicas:
suma, resta, multiplicación división, potencia y módulo. Las funciones de operación se importan desde el módulo operaciones
y se ejecutan de acuerdo con la selección del usuario.

El programa valida entradas numéricas y opciones del menú, mostrando mensajes claros en caso de errores.'''
from operaciones import suma, resta, multiplicacion, division, potencia, modulo

def menu():
    """
    Muestra un menú interactivo para seleccionar y ejecutar operaciones aritméticas.
    
    Este menú se ejecuta en un ciclo infinito hasta que el usuario seleccione la opción para salir (opción 7). 
    El programa valida tanto la opción elegida como las entradas numéricas proporcionadas por el usuario.
    
    Flujo del menú:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División.
    5. Potencia
    6. Módulo
    7. Salir del programa

    Manejo de errores:
    -Si el usuario ingresa una opción inválida, se muestra un mensaje y se reinicia el menú.
    -Si los valores ingresados no son numéricos, se muestra un mensaje y se solicita nuevamente la entrada.

    No retorna valores. Únicamente imprime resultados en pantalla. 
    """
    while True:
        print("\n Calculadora de Operaciones Basicas")
        print("Presione 1 si desea realizar una: SUMA")
        print("Presione 2 si desea realizar una: RESTA")
        print("Presione 3 si desea realizar una: MULTIPLICACION")
        print("Presione 4 si desea realizar una: DIVISION")
        print("Presione 5 si desea realizar una: POTENCIA")
        print("Presione 6 si desea realizar un: MODULO")
        print("Presione 7 si desea SALIR del programa")

        '''Solicita al usuario la eleccion de una opcion'''
        opcion = input("Seleccione una opcion del 1 al 7: ")

        '''Si el usuario eligio la opcion 7, el programa se cierra'''
        if opcion == "7":
            print("Saleindo de calculadora...")
            break
        
            '''Si el usuario elige una opcion diferente a las mostradas en el menu: se imprime un aviso'''
        if opcion not in ["1", "2", "3", "4", "5", "6"]:
            print("\n --AVISO: La opcion seleccionada NO EXISTE:")
            print("Vuelva a intentar con una opcion del 1 al 5--")
            continue


        # El programa captura los valores de a(flotante) y b(flotante) que proporciona el usuario
        try:
            '''El usuario ingresa los valores (a y b)'''
            a = float(input("Ingresa el primer valor: "))
            b = float(input("Ingresa el segundo valor: "))
            '''Si el usuario no ingresa un numero de manera correcta. El programa imprime un aviso'''
        except ValueError:
            print("\n --Error: Alguno o algunos de los valores que ingresaste no es valido")
            print("Intenta con un valor de tipo FLOTANTE--")
            continue

# Ejecutar la operación seleccionada 
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
#Si el usuario selecciona la opcion 5, entonces el programa realiza una potencia
        elif opcion == "5":
            print("Resultado:", potencia(a, b))
 #Si el usuario selecciona la opcion 6, entonces el programa obtiene el modulo de un numero
        elif opcion == "6":
            print("Resultado:", modulo(a, b))


# Bloque de ejecución principal: llama al menú
if __name__ == "__main__":
    menu()