nombre_usuario = input('cual es tu nombre?:')

print(f"{nombre_usuario} ingresa un numero del 1 al 100, tienes solo 8 intentos para adivinarlo:")


from random import *
aleatorio = randint(1,100)

numero_usuario = int(input("ingresa tu numero:"))

vida = 8

while vida > 1:
    if numero_usuario < 1:
        vida = vida -1
        print(f"{nombre_usuario} este numero esta por debajo del rango entregado el rango es (1-100), te quedan {vida} vidas")
        numero_usuario = int(input("ingresa tu numero:"))
    elif numero_usuario > 100:
        vida = vida - 1
        print(f"{nombre_usuario} este numero esta por encima del rango entregado, el rango es (1-100), te quedan {vida} vidas")
        numero_usuario = int(input("ingresa tu numero:"))
    elif numero_usuario < aleatorio:
        vida = vida - 1
        print(f"tu numero es menor al numero secreto, te quedan {vida} vidas")
        numero_usuario = int(input("ingresa tu numero:"))
    elif numero_usuario > aleatorio:
        vida = vida - 1
        print(f"tu numero es mayor al numero secreto, te quedan {vida} vidas")
        numero_usuario = int(input("ingresa tu numero:"))
    elif numero_usuario == aleatorio:
        print(f"felicidades, ganaste. te quedaron {vida} vidas.")
        break
if numero_usuario != aleatorio:
    print(f'no te quedan mas vidas, el numero secreto es {aleatorio}')
