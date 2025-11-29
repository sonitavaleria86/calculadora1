from operaciones import suma, resta, multiplicacion, division, potencia

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
        print("Presione 6 si desea SALIR del programa")

        opcion = input("Seleccione una opcion del 1 al 6: ")

        if opcion == "6":
            print("Saleindo de calculadora...")
            break

        if opcion not in ["1", "2", "3", "4", "5"]:
            print("\n --AVISO: La opcion seleccionada NO EXISTE:")
            print("Vuelva a intentar con una opcion del 1 al 5--")
            continue

        # Captura los valores de a y b que decidio el usuario
        try:
            a = float(input("Ingresa el primer valor: "))
            b = float(input("Ingresa el segundo valor: "))
        except ValueError:
            print("\n --Error: Alguno o algunos de los valores que ingresaste no es valido")
            print("Intenta con un valor de tipo FLOTANTE--")
            continue

        # Operaciones 
        if opcion == "1":
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("Resultado:", division(a, b))
        elif opcion == "5":
            print("Resultado:", potencia(a, b))


# Llama al menú
if __name__ == "__main__":
    menu()