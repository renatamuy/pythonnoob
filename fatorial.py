numero = int(input("Calcular fatorial para qual número? "))

fatorial= 1

while numero > 1:
    fatorial = fatorial * numero
    numero = numero - 1


print(fatorial)


