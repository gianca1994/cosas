from time import time

inicio = time()

print("--------------")
print("Programa para calcular la clave secreta")
print("--------------\n")
clave = int(input("Hola ingresa la clave Publica: "))
q = int(input("Ingresa el numero primo q: "))
a = int(input("Ingresa el valor de la raiz primitiva: "))

for i in range(q):
    ck = (a ** i) % q
    if clave == ck:
        resultado = i
        i = q

print(" \n La clave privada es: ", resultado)

final = time()

tiempo = (final - inicio)

print("\n El tiempo de computo es: ", tiempo)
