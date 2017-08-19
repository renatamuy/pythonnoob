numero = int(input("Calcular fatorial para qual número? "))

fatorial= 1

if numero < 0:
   print("Deve ser positivo senão não roda")
elif numero == 0:
   print("fatorial = 1")
else:
   for i in range(1,numero + 1):
       fatorial = fatorial*i

print(fatorial)
