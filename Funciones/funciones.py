
#Funciones sirven para guardar una secuencia de codigo bajo
#un nombre para poder ejecutarlas haciendo referencia a ese nombre en cualquier momento

#Definimos una funcion
def saludo_sectario(nombre):
    #para darle vuelta a una string es ::-1
    print("Hola {}".format(nombre[::-1]))


#Llamamos a la funcion
saludo_sectario("Ricardo")
saludo_sectario("Alfredo Solano")
saludo_sectario("Sergio Hernandez")
