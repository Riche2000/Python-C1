#Librerias
from time import sleep

#Funciones recursivas
def medir_largos(iterable,*args,sumar_todo=False):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(iterable)

def main():
    print(medir_largos("hola"))
    print(medir_largos("hola","como","estas",sumar_todo=True))

if __name__ == "__main__":
    main()


"""
def medir_largos(iterable, *args, sumar_todo=False):
    #Sumar solo es para la funcion medir_largos
    def sumar(numero1,numero2):
        return numero1 + numero2
    print("Suma total: ",sumar(1,2))

    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)


def main():
    print(medir_largos("Hola"))
    print(medir_largos("hola","como","estas"))

if __name__ == "__main__":
    main()
"""

"""
def sumar_uno(a):
    print(a)
    a += 1
    if a != 100:
        sumar_uno(a)

def main():
    sumar_uno(1)

if __name__ == "__main__" :
    main()
"""
"""
def a():
    print("C")
    #Sleep es para dar tiempos
    sleep(1)
    a()

def b():
    print("B")
    sleep(1)
    c()

def a():
    print("A")
    sleep(1)
    b()

def main():
    a()


if __name__ == "__main__":
    main()
"""