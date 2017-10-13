

def MinMax(temperaturas):
    print("A menor temp do mês foi: ", minima(temperaturas), "C.")
    print("A maior temp do mês foi: ", max(temperaturas), "C.")

def minima(temps):
    min = temps[0] #nao sei como começo. se começa como valor 0 dá erro
    i = 1 #como ja tem o temps[0] pode comecar com 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

#def max(temps):

#refatoracao é melhorar o código

def maxima(temps):
    max = temps[0] #nao sei como começo. se começa como valor 0 dá erro
    i = 1 #como ja tem o temps[0] pode comecar com 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max


###

def testa_minima():
    print("Iniciando teste")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 10], 0)
    teste_pontual([33, 32, 30, 29,22], 22)
    teste_pontual([-33, 32, 30, 29,22], -33)
    print("Finalizando teste")

'''refatorando''' 
def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("O valor esperado era", valor_esperado, ".Valor calculado: ", valor_calculado)
    

