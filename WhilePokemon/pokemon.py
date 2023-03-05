#Librerias
from random import randint
import os

#Variables
#Las variables con letras MAYUSCULAS es una constante, no se puede modificar su valor
VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_SQUIRTLE = 100

TAMANIO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    #Se desenvuelven los turnos de combate

    #Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        #Le bajamos la vila a squirtle 10 puntos
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        #Le bajamos vida a squirtle 11 puntos
        vida_squirtle -= 11

        #Para que no salga la vida negativa
        if vida_pikachu < 0:
            vida_pikachu = 0
        if vida_squirtle < 0:
            vida_squirtle = 0

    #Barra de vida la pasamos a entero para poder hacer la multiplicacion
    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("#"*barras_de_vida_pikachu," "*(TAMANIO_BARRA_VIDA-barras_de_vida_pikachu),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))
    barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                               vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n\n")
    os.system("cls")

    #Turno Squirtle
    print("Turno Squirtle")

    ataque_squirtle =None
    #Usamos una lista
    while ataque_squirtle not in ["P","A","B","N"]:
        ataque_squirtle = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        #Baja la vida de pikachu 10 puntos
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada...")

        # Para que no salga la vida negativa
        if vida_pikachu < 0:
            vida_pikachu = 0
        if vida_squirtle < 0:
            vida_squirtle = 0

        barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
        print("Pikachu:    [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_pikachu),
                                                  vida_pikachu, VIDA_INICIAL_PIKACHU))
        barras_de_vida_squirtle = int(vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
        print("Squirtle:   [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_VIDA - barras_de_vida_squirtle),
                                                   vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        input("Enter para continuar...\n\n")
        os.system("cls")

if vida_pikachu > vida_squirtle:
    print("¡Pikachu Gana!")
else:
    print("¡Squirtle Gana!")