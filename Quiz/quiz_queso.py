#La \n Significa enter

titulo = "Bienvenido al test sobre el queso"

print("\n"+titulo+"\n"+"-"*len(titulo)+"\n")

puntuacion = 0

#string multilinea (""" """)
opcion = input("""Pregunta 1: ¿Que haces cuando ves una tabla de quesos?
            A - Salgo corriendo
            B - Prubo uno de los quesos o incluso varios
            C - No puedo evitar devorarla
            \nOpcion: """)

#Comprueba la A
if opcion == "A":
    puntuacion += 0
#Comprueba la B
elif opcion == "B":
    puntuacion += 5
# Comprueba la C
elif opcion == "C":
    puntuacion += 10
#Si no es eninguno de los casos
else:
    print("Las opciones posibles son A, B y C")
    #Terminamos el programa
    exit()

opcion = input("""Pregunta 2: ¿Como te gusta la hamburguesa?
            A - Sin queso
            B - Con queso
            C - Pan y queso
            \nOpcion: """)

#Comprueba la A
if opcion == "A":
    puntuacion += 0
#Comprueba la B
elif opcion == "B":
    puntuacion += 5
# Comprueba la C
elif opcion == "C":
    puntuacion += 10
#Si no es eninguno de los casos
else:
    print("Las opciones posibles son A, B y C")
    #Terminamos el programa
    exit()

opcion = input("""Pregunta 3: ¿Eres intolerante a la lactosa?
            A - Si
            B - A veces
            C - No
            \nOpcion: """)

#Comprueba la A
if opcion == "A":
    puntuacion += 0
#Comprueba la B
elif opcion == "B":
    puntuacion += 5
# Comprueba la C
elif opcion == "C":
    puntuacion += 10
#Si no es eninguno de los casos
else:
    print("Las opciones posibles son A, B y C")
    #Terminamos el programa
    exit()

if puntuacion >= 25:
    print("Resultado: Felicidades, eres fanatico de los quesos")
elif puntuacion >=15:
    print("Resultado: Felicidades, eres una persona que le gusta el queso")
else:
    print("Resultado: Felicidades, no te gusta el queso")