
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: División por cero"

def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingresa el número de la operación: ")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", suma(a, b))
    elif opcion == "2":
        print("Resultado:", resta(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")

calculadora()
