#random es para generar numeros aleatorias
import random

#Numero aleatorio del 1 al 10
numero_ganador = random.randint(1, 10)
numero_elegido = int(input("Elige un numero: "))

if numero_elegido == numero_ganador:
    print("¡Has ganado!")

if numero_elegido > 10:
    print("Te has pasado un poco... Era entre 1 y 10")

if numero_elegido < 1:
    print("Te has quedad corto")

if numero_elegido == 666:
    print("Has elegido el numero de la bestia")


print("El numero ganador era: {}".format(numero_ganador))