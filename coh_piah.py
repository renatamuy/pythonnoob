'''Tamanho médio de palavra: Média simples do número de caracteres por palavra.
Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
Tamanho médio de sentença: Média simples do número de caracteres por sentença.
Complexidade de sentença: Média simples do número de frases por sentença.
Tamanho médio de frase: Média simples do número de caracteres por frase.'''
'''Lista de funções
OK def le_assinatura():
OK def le_textos():
OK def separa_sentencas(texto):
OK def separa_frases(sentenca):
OK def separa_palavras(frase):
OK def n_palavras_unicas(lista_palavras):
OK def n_palavras_diferentes(lista_palavras):
def compara_assinatura(as_a, as_b): IMPLEMENTAR
def calcula_assinatura(texto): IMPLEMENTAR
def avalia_textos(textos, ass_cp): IMPLEMENTAR
Funções auxiliares:
def tamanho_medio_palavras(palavras):
def relacao_type_token(palavras):
def razao_hapax_legomana(palavras):
def tamanho_medio_de_sentenca(sentencas):
def complexidade_de_sentenca(lista_frases, sentencas):
def tamanho_medio_de_frase(lista_frases):
def main()
10 (ou 9) funções para fazer.................!


'''
####################################################################
import re
'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
'''funções definidas por mim'''
'''Tamanho médio de palavra: Média simples do número de caracteres por palavra.'''
def tamanho_medio_palavras(palavras): 
def relacao_type_token(palavras):
def razao_hapax_legomana(palavras):
def tamanho_medio_de_sentenca(sentencas):
def complexidade_de_sentenca(lista_frases, sentencas):
def tamanho_medio_de_frase(lista_frases):
    
def compara_assinatura(as_a, as_b): 
    #comparação de listas
    #if ( ass1 == ass2 ):
    #le_assinatura()
    #as_a = le_assinatura()
    #as_b = calcula_assinatura(texto)
    #return ass_cp #lista
    #    abs (differenca( traços)) / 6
    #    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
     int(input("Entre com um texto:"))
    #tam_medio = wal =  sum tamanhos  / numero de palavras
    #typetoken = ttr = numero de palavras únicas / total de palavras
    #hapaxlegomana = hlr = numero de palavras singletons / total de palavras
    #tammediosentenca = sal = soma de todos os caracteres sem separadores / numero de sentencas
    #complexidade = sac = numero toral de frases / numero de sentencas
    #tammediofrase = pal = soma de caracteres sem separadores / numero de frases

    #return [wal, ttr, hlr, sal, sac, pal]
    ass = []
    ass.append
    pass
   
def avalia_textos(textos, ass_cp):
    #textos = []
    #textos = le_textos()
    #for i in textos:
    #    ass_cp = compara_assinatura(as_a, as_b) #as_a e as_b são as coisas que rodam?
    #    compara_assinatura(orig,i)
    #recebe_comparacao = recebe.comparacao.append(compara_assinatura(i,j))
    return(textos[infectado_POSICAO])
    #print("O autor do texto", textos[infectado_POSICAO], "está infectado com COH-PIAH")
    pass
    min = ass_cp[0] 
    k = 1 #como ja tem o temps[0] pode comecar com 1
    while k < len(ass_cp):
        if ass_cp[k] < min:
            min = ass_cp[i]
        k = k + 1
    return min #valor ou posicao do valor?  ira retorna a numeração do texto que esta associada a o valor encontrado.'''


    
