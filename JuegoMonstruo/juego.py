import random

numero_ganador = random.randint(1, 6)

titulo = "Juego del Monstruo"
print("\n"+titulo+"\n"+"-"*len(titulo)+"\n"
      "Despiertas en una casa abandonada es de noche y no sabes como llegaste ahí \n"
      "caminas por la habitación a obscuras y encuentras una linterna tirada en el suelo. \n"
      "Descubres que en la habitación hay dos puertas, una del lado izquierdo y la otra del lado derecho."
      "¿Qué puerta eliges?"
      )

opcion = input("[A] Puerta Izquierda | [B] Puerta Derecha: ")

if opcion == "A":
    print("Entras por la puerta izquierda y ves una sombra a lo lejos de la habitación, ¿Te acercas a averiguar que es?")
    opcion = input("[A] Te acercas [B] Lo piensas un poco: ")

    if opcion == "A":
        print("Es el monstruo parado y te come\nFIN")
    elif opcion == "B":
        print("Despues de pensarlo un poco encuentras un dado tirado en el sulo ¿Lo tomas?")
        opcion = input("[A] Si | [B] No: ")

        if opcion == "A":
            print("te agachas y tomas el dado. El monstruo te descubre y te propone un acuerdo...\n"
                  "Si tiras el dado y sale el número 2 te deja ir ¿Aceptas el acuerdo?")
            opcion =input("[A] Si | [B] No: ")

            if opcion == "A":
                if numero_ganador == 2:
                    print("¡Cayo el número {}!".format(numero_ganador))
                    print("El monstruo te deja ir... FIN")
                if numero_ganador != 2:
                    print("¡Cayo el número {}!".format(numero_ganador))
                    print("El monstruo te come... FIN")
            elif opcion == "B":
                print("EL monstruo te come.")

if opcion == "B":
    print("Entras por la puerta derecha, corres como gallina...\n"
          "Afortunadamente, encuentras la salida y logras huir... FIN")