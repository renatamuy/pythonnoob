
print("Digite uma seq de valores e para parar de somar digite zero")
soma = 0 

valor = 1
while valor != 0:
	valor = int(input("Digite um valor a ser somado: "))
	soma=  soma + valor
print("A soma dos valores digitados é:", soma)
