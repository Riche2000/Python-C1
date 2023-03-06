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

map_objects = [[2,3],[5,4],[3,4],[10,6]]

while True:

    #Draw Map
    print("+"+"-"*MAP_WIDTH*3+"+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|",end="")
        #A cada una de las iteraciones que tenga en mi for voy a tern un número desde el 0 hasta 19
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)


            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+"+"-"*MAP_WIDTH*3+"+")

    #Ask usar where he wants to move

    #direction = input("¿Oonde te quieres mover? [WASD]: ")
    #usamos la libreria readchar
    direction = readchar.readchar()
    print(direction)

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break

    #Para borrar la pantalla apra iwndows es cls, mac o linux es cleaar
    os.system("cls")
