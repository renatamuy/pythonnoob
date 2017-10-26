print("Digite um número de quatro dígitos de seu interesse")

valor = input("Digite um valor a ser somado: ")
valor= int(valor)
primeiro = valor // 1000
segundo = (valor // 100) % 10
terceiro =  (valor % 100) // 10
quarto = valor % 10

soma= primeiro+ segundo + terceiro + quarto

print("A soma dos quatro dígitos é", soma)

