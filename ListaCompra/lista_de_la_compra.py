
#Variables
#Lista
lista_de_la_compra = []
input_de_usuario = None

print("Programa lista de la compra\n")

#Siempre se va a ejecutar hasta que yo decida el brake
while True:
    input_de_usuario = input("¿Que desea comprar? [Q] para salir: ")
    if input_de_usuario == "Q":
        #Si es igual a Q no hago nada pass es para que no haga nada y break es para salirse del while
        break
    #Comprobamos que este en la lista
    elif input_de_usuario in lista_de_la_compra:
        print("{} ya esta en la lista".format(input_de_usuario))
        #Si no esta en la lista
    else:
        if input("¿Seguro que quiere añadir {} a la lista de la compra? [S/N]: ".format(input_de_usuario)) == "S":
            lista_de_la_compra.append(input_de_usuario)

print("La lista de la compra es: ")
print(lista_de_la_compra)