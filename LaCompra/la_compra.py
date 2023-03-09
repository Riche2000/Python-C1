SALIR = "SALIR"


def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]]".format(SALIR))


def guardar_lista_a_disco(lista_compra):
    nombre_fichero = input("Como quieres que se llame el archivo? ")
    with open(nombre_fichero + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe!")
    else:
        lista_compra.append(item_a_guardar)


def incrementar(num):
    num += 1
    return num


def main():
    lista_compra = []

    input_usuario = preguntar_producto_usuario()

    numero = 8
    incrementar(numero)
    incrementar(numero)
    incrementar(numero)

    while input_usuario != SALIR:
        guardar_item_en_lista(lista_compra, input_usuario)
        print("\n".join(lista_compra))
        input_usuario = preguntar_producto_usuario()

    guardar_lista_a_disco(lista_compra)


if __name__ == "__main__":
    main()