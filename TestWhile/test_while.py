#Para que pregunte sin parar hasta que me de una respuesta correcta usamos el while

#La variable None es in NoneType osea una variable sin valor
##respuesta = None

##while respuesta != "A" and respuesta != "B" and respuesta != "C":

 ##   respuesta = input("¿Que opcion prefieres [A, B, C]? ")

##if respuesta == "A":
##    print("Has elegido bien.")
##elif respuesta == "B":
##    print("Podrias haber elegido mejor.")
##elif respuesta == "C":
##    print("Elegiste mal.")
##else:
##    print("No me has dado una respuesta congruente")

## ------------------------------------------------------
numero = 12

while numero > 1:
    print("Mi numero {} es mayor que 1".format(numero))
    numero -= 1
