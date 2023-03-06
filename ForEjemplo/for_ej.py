""""
"#Ejemplo
texto_usuario = "Hola, me llamo Ricardo. ¿Tu como te llamas?"

#Output esperado
espacios = 7
puntos = 1
comas = 1
"""

texto_usuario = input("Introduzca un texto: ")
espacios = 0
puntos = 0
comas = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Estacios: {}, Puntos: {} y Comas {}".format(espacios, puntos, comas))
