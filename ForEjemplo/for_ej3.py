"""
# Numero elegido por el usuario: 2

# Output esperado
2x1 = 2
2x2 = 4
2x3 = 6
...
"""
        #Pedimos el número en entero
numero = int(input("Numero a multiplicar: "))

for n in range(1,11):
    # % Es lo que sobra de la division 
    # if n % 2 == 0: Nos sireve para que solo muestre los multiplos de 2
    if n % 2 == 0:
        print("{} x {} = {}".format(n, numero, n * numero))