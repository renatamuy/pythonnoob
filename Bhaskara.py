import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    ad = float(input("Digite o valor de a: "))
    bd = float(input("Digite o valor de b: "))
    cd = float(input("Digite o valor de c: "))
    imprime_raizes(ad, bd, cd)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1= (-b + math.sqrt(d)) / (2 * a)
        print(" A unica raiz é: ", raiz1)
    else:
            if d < 0:
                    print("Sem raízes reais ")
            else:
                    raiz1 = (-b + math.sqrt(d)) / (2 * a)
                    raiz2 = (-b - math.sqrt(d)) / (2 * a)
                    print("Raiz 1: ")
                    print("Raiz 2: ")
                    
