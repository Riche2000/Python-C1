#Definimos una lista
#iterables puedes ser una lista, una tupla, ouna string
lista_de_la_compra = {"Leche","Azucar","Oreos"}
frase = "Hola, hoy estoy aprendiendo Python"
vocales = ["a","e","i","o","u"]
numero_vocales = 0

#for recorre un iterable
for item in lista_de_la_compra:
    #item nos selecciona 1 por uno
    print("Voy a comprar {}".format(item))

for letra in frase:
    if letra in vocales:
        print("He encontrado una '{}'".format(letra))
        numero_vocales += 1

print("Vocales encontradas: {}".format(numero_vocales))