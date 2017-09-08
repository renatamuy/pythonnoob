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
