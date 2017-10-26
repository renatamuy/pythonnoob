import math

x = int(input("Digite um valor de longitude: "))
y = int(input("Digite um valor de latitude: "))
x1 = int(input("Digite um valor de longitude do segundo ponto: "))
y1 = int(input("Digite um valor de latitude do segundo ponto: "))

distancia= math.sqrt((x1- x ) ** 2 + (y1- y)** 2)

if(distancia >= 10):
    print("longe")
else:
    print("perto")
