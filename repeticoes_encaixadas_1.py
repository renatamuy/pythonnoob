def desenha(linha):    
    while linha > 0:
        coluna = 1
        while coluna <= linha:
            print('*', end = "")
            coluna = coluna + 1
        print()
        linha = linha - 1

desenha(5)

###########

print()
print()
print()
print()
print()

altura = 5
linha = 1

while linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*", end = "")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1


x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        print(" Iteração")
        print(y)
        y = y + 1       
    x = x + 1

'''x < 3 em duas situações.
   y <= 4 em 5 situações = 0 1 2 3 4
   Então você tem 2 vezes 5 valores no aninhamento. 10 vezes é iterado'''
