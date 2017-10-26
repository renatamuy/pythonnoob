numero = int(input("Digite um número inteiro"))

teste = numero % 3
teste2 = numero % 5

if(teste == 0 and teste2 == 0):
    print("FizzBuzz")
else:
   print(numero) 

    
