nombre = input("dime cual es tu nombre:")


ventas =input("cuanto hiciste este mes:")

ventas= int(ventas)
comision = round(ventas * 13 / 100,2)

print(f"Hola {nombre} tu comisione es ${comision}")




nombre = input("dime cual es tu nombre:")
ventas =int(input("cuanto hiciste este mes:"))

comision = ventas * 13 / 100
comision = round(comision,2)

print(f"Hola {nombre} tu comisione es ${comision}")
