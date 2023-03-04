dolar_euro = 0.94
libra_euro = 1.13

opcion = input("¿Que decea hacer?\n"
               "A - Convertit de dolar a euro\n"
               "B - COnvertir de euro a dolar\n"
               "C - Convertir de libra a euro\n"
               "D- Convertir de euro a libra\n"
               "Opcion: ")

texto_usuario = "Introduzca la cantidad de {} a convertir: "

if opcion == "A":
    cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en euros es {}".format(cantidad_de_dinero * dolar_euro))

elif opcion == "B":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en dolares es {}".format(cantidad_de_dinero / dolar_euro))

elif opcion == "C":
    cantidad_de_dinero = float(input(texto_usuario.format("libras")))
    print("La cantidad en euros es {}".format(cantidad_de_dinero * libra_euro))

elif opcion == "D":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en libras es {}".format(cantidad_de_dinero / libra_euro))

else:
    print("No ha elegido ninguna opcion valida ")