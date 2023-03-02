a = int(input("Digita un número: "))
b = int(input("Digita un segundo número: "))
c = int(input("Digita un tercer número: "))

#Para pode imprimir en patnalla un string y un numero seria:
# "Tu numero es : {}".format(5)

#print("El número más grande entre {}, {} y {} es: {}".format(a, b, c, max(a,b,c)))
#print("El número más pequelo entre {}, {} y {} es: {}".format(a, b, c, min(a,b,c)))

print("El número más grande entre {}, {} y {} es {} y el más pequeño es {}".format(a, b, c,
                                                                                max(a,b,c),
                                                                                min(a,b,c)))