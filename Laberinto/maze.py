#librerias para instalar cosas es con alt + enter
import os
import readchar

POS_X = 0
POS_Y = 1

#Ancho del mapa
MAP_WIDTH = 20
#Altura del mapa
MAP_HEIGHT = 15

#              x, y
my_position = [6,3]

while True:

    #Draw Map
    print("+"+"-"*MAP_WIDTH*3+"+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|",end="")
        #A cada una de las iteraciones que tenga en mi for voy a tern un número desde el 0 hasta 19
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ",end="")
            else:
                print("   ",end="")
        print("|")

    print("+"+"-"*MAP_WIDTH*3+"+")

    #Ask usar where he wants to move

    #direction = input("¿Oonde te quieres mover? [WASD]: ")
    #usamos la libreria readchar
    direction = readchar.readchar()
    print(direction)

    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        break

    #Para borrar la pantalla apra iwndows es cls, mac o linux es cleaar
    os.system("cls")

