print("Me voy a la cocina")
print("Abro la nevera")

hay_leche = input("¿Hay leche? (S/N) ")
hay_nesquik = input("¿Hay Nesquik? (S/N) ")

#Condicionales
# dos == es una comparacion y so es solo un = es una asignacion
# != significa si no es igual a
#or comprueba si una de las dos es falsa
#Si hay_leche es distinto de S o si hay_nesquik es distinto de S voy al super
if hay_leche != "S" or hay_nesquik != "S":
    #Los cuatro espacios son para que Python sepa que es parte del if
    print("Voy al super...")
    if hay_leche != "S":
        print("Compro leche")
    if hay_nesquik != "S":
        print("Compro Nesquik")
print("Ponemos la leche en el vaso")
print("Ponemos Nesquik en el vaso")
print("Mezclamos")

