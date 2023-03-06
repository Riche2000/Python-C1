#librerias para instalar cosas es con alt + enter
import os
import random
import readchar

POS_X = 0
POS_Y = 1

#Ancho del mapa
MAP_WIDTH = 20
#Altura del mapa
MAP_HEIGHT = 15

NUM_OF_MAP_OBJECTS = 11

#              x, y
my_position = [6, 3]
tail_length = 0
tail = []
map_objects = []

#Generate random objects
#Mientras el largo del map_ojects
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    #COmprobamos que n se repitna las posiciones
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

# Main Loop
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
            for tail_pice in tail:
                if tail_pice[POS_X] == coordinate_x and tail_pice[POS_Y] == coordinate_y:
                    char_to_draw = "@"
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+"+"-"*MAP_WIDTH*3+"+")
    print("La cola {}".format(tail))

    #Ask usar where he wants to move

    #direction = input("¿Oonde te quieres mover? [WASD]: ")
    #usamos la libreria readchar
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break

    #Para borrar la pantalla apra iwndows es cls, mac o linux es cleaar
    os.system("cls")

