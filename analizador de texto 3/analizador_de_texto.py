texto = input("ingresa un texto a elección:".lower())
letras = []

texto = texto.lower()

letras.append(input("ingresa la primera letra: ").lower())
letras.append(input("ingresa la segunda letra: ").lower())
letras.append(input("ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1}")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2}")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3}")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"hemos encontrado {len(palabras)}")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto [-1]
print(f"la letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"si ordenamos tu texto al reves va a decir: {texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_pythone = 'python' in texto
dic = {True:"si", False:"no"}
print(f"la palabra 'python' {dic[buscar_pythone]} se encuentra en el texto")

