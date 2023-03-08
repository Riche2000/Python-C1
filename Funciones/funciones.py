
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

def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
    return largo

largo_de_la_string = largo_string("Hola mundo")

print(largo_de_la_string)

def main():
    print("Hola mundo")

#Ejuectuamos la funcion para importar se usa __funcion__
if __name__ == "__main__":
    main()