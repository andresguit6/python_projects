nombre = ""
apellido = ""
balance = 0
retirar_balance = 0
juego = True



class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def mostrar_datos_cliente(self):
        return f"Usted es un cliente preferente.\nSu numero de cuenta es {cliente1.numero_cuenta} su balance es {cliente1.balance}:"

    def depositar(self):
        global balance
        deposito = input("cuanto quiere depositar?:")
        balance = balance + int(deposito)
        continuar_preguntando()


    def retirar(self):
        global balance
        global retirar_balance

        if balance == 0:
            print("no puedes retirar")
        else:
            retirar_balance = int(input("cuanto quiere retirar?:"))
            if balance >= retirar_balance:
                balance = balance - retirar_balance
            else:
                print("no puedes retirar esa cantidad")

        continuar_preguntando()



def informacion_cliente():
    global nombre
    global apellido
    print("para iniciar, ingrese su información")
    nombre = input("ingrese su nombre:")
    apellido = input("ingrese su apellido:")
    return f"Bienvenido {nombre} {apellido}"


def continuar_preguntando():
    print(f"su saldo es {balance}")
    print("Que quieres hacer? :")
    print("1. Depositar")
    print("2. Retirar")
    print("3. salir")

    opcion = input("Ingresa el número de la opción que deseas escoger (1, 2, o 3): ")



    if opcion == "1":
        return cliente1.depositar()
    elif opcion == "2":
        return cliente1.retirar()
    elif opcion == "3":
        print("saliendo del sistema")
    else:
        print("opcion no valida, debes selecionar las opciones (1,2,3)")
        return continuar_preguntando()
        pass


print(informacion_cliente())
print("\n")
cliente1 = Cliente(nombre, apellido, "14.594.124", balance )
print(cliente1.mostrar_datos_cliente())
print("\n")

continuar_preguntando()