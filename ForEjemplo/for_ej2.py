"""
#Ejemplo
texto usuario = "Hola, me llamo Ricardo. ¿Tu como te llamas?"

#Output esperado
mayusculas = 3
"""
#Librerias
import string

texto_del_usuario = input("Introduzca un texto: ")
print(string.ascii_uppercase)
#Contador
letras_mayusculas = 0

for letra in texto_del_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("La mayusculas son: {}".format(letras_mayusculas))
