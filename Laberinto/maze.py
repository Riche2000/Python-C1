POS_X = 0
POS_Y = 1

#Ancho del mapa
MAP_WIDTH = 20
#Altura del mapa
MAP_HEIGHT = 15

#              x, y
my_position = [6,3]
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
