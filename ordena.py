numero = int(input("Digite um número inteiro"))
numero2 = int(input("Digite outro número inteiro"))
numero3 = int(input("Digite mais um número inteiro"))

teste1 = numero  <= numero2
teste2 = numero2  <= numero3

if(teste1 == True and teste2 == True):
    print("crescente")
else:
   print("não está em ordem crescente") 

    
