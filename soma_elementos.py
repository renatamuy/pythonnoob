'''Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número
inteiro correspondente à soma dos elementos da lista recebida.'''


def soma_elementos(lista):
    soma = 0
    for i in range(0, len(lista)):
        valor = lista[i]
        soma = soma + valor
    return(soma)
