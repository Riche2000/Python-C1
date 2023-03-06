"""
# Números usuario
numeros = [1,2,3,4,5,6]

#Output
numero_mas_pequeño: 1
numero_mas_grande: 6
"""

"""
#Manera 1 de transformar los números a enteros
#Lista
numeros_introducidos = input("Introduzca los números separados por coma: ")
#Rompe el string en muchos strings separados por una coma
numeros_de_usuario = numeros_introducidos.split(",")
#Numeros int
numeros_de_usuario_limpios = []

#Transformamos la string en números int
for numero in numeros_de_usuario:
    numeros_de_usuario_limpios.append(int(numero))
"""
#Segunda forma
numeros_introducidos = input("Introduzca los números separados por coma: ")
#List Comprehesion o Comprension de listas
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

"""
numero_introducido = int(input("Introduzca un número en la lista: "))
# .append Agrega un ítem al final de la lista.
numeros_de_usuario.append(numero_introducido)

while input("Desea introducir más numeros? [S/N]: ") == "S":
    numero_introducido = int(input("Introduzca un número en la lista: "))
    # .append Agrega un ítem al final de la lista.
    numeros_de_usuario.append(numero_introducido)
"""

numero_pequenio = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

#recorremos la lista
#Filtrado de listas
#Por ejemplo del 1 al 3 seria [1:3]
for numero in numeros_de_usuario[1:]:
    if numero_pequenio > numero:
        numero_pequenio = numero
    if numero_grande < numero:
        numero_grande = numero

print("Numero grande: {}, Numero pequeño {}".format(numero_grande, numero_pequenio))