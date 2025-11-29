from operaciones import suma, resta, multiplicacion, division, potencia, modulo

def menu():
    """
    Muestra al usuario la operacion que desea realizar.
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

        '''Si el usuario eligio la opcion 5, el programa se cierra'''
        if opcion == "7":
            print("Saleindo de calculadora...")
            break
        
            '''Si el usuario elige una opcion diferente a las mostradas en el menu: se imprime un aviso'''
        if opcion not in ["1", "2", "3", "4", "5", "6"]:
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
            print("\n --Error: Alguno o algunos de los valores que ingresaste no es valido")
            print("Intenta con un valor de tipo FLOTANTE--")
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
#Si el usuario selecciona la opcion 5, entonces el programa realiza una potencia
        elif opcion == "5":
            print("Resultado:", potencia(a, b))
 #Si el usuario selecciona la opcion 6, entonces el programa obtiene el modulo de un numero
        elif opcion == "6":
            print("Resultado:", modulo(a, b))


# Llama al menú
if __name__ == "__main__":
    menu()