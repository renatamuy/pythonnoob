n = int(input("Digite um número inteiro: "))

#sempre zerar o objeto armazenador em while e criar o contador

soma= 0

while n > 0: 
        atual= n%10
        soma= atual+ soma
        n= n//10

print("A soma dos dígitos é :", soma)




