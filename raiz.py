import math

print("Lembre-se que uma equação quadrática tem três coeficientes quadráticos, formando algo do tipo: a**2 + b*x+ c= 0")

a= float(input("Qual seu a? "))
b= float(input("Qual seu b? "))
c= float(input("Qual seu c? "))

delta = (b ** 2 - 4* a * c )

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2* a) 
    print("A única raiz é", raiz1, "!")
else:
    if delta < 0:
        print("Sorry. Esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2* a)
        raiz2 = (-b - math.sqrt(delta)) / (2* a)
        print("As raízes da equação são", raiz1,"e", raiz2, "!")
