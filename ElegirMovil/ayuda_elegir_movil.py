opcion = input("¿iOS [I] o Android [A]? ")

movil_ideal = "Ninguno"

if opcion == "A":
    opcion = input("¿Tienes Dinero? [S/N]: ")
    if opcion == "S":
        opcion = input("¿Te importa la camara del movil? [S/N]: ")
        if opcion == "S":
            movil_ideal = "Samsung S23"
        else:
            movil_ideal = "Android calidad-precio (Xiaomi)"
    else:
        movil_ideal = "Android Chino de $100"
elif opcion == "I":
    opcion = input("¿Tienes Dinero? [S/N]: ")
    if opcion == "S":
        movil_ideal = "iPhone Pro Max"
    else:
        movil_ideal = "iPhone 7"

print("Tu movil ideal es "+ movil_ideal)