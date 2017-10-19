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
def compara_assinatura(as_a, as_b): 
def calcula_assinatura(texto): 
def avalia_textos(textos, ass_cp): 
OK19 def tamanho_medio_palavras(palavras):
OK19 def relacao_type_token(palavras):
OK19 def razao_hapax_legomana(palavras):
OK19 def tamanho_medio_de_sentenca(sentencas):
OK19 def complexidade_de_sentenca(lista_frases, sentencas):
OK19 def tamanho_medio_de_frase(lista_frases):
def main()
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

def n_palavras_unicas(palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

'''funções definidas por mim'''
'''Tamanho médio de palavra: Média simples do número de caracteres por palavra.'''

def tamanho_medio_palavras(palavras):
    soma = 0
    for i in range(0, len(palavras)):
        valor = len(palavras[i])
        soma = soma + valor
    return(soma / len(palavras) ) 
	
'''Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo
total de palavras.'''
    
def relacao_type_token(palavras):
    difs = n_palavras_diferentes(palavras)
    return ( difs / len(palavras))


'''vazão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo
número total de palavras.'''

def razao_hapax_legomana(palavras): 
    return ((n_palavras_unicas(palavras)) / len(palavras))

'''Tamanho médio de sentença:Média simples do número de caracteres por sentença.'''

def tamanho_medio_de_sentenca(sents):
    sents = separa_sentencas(texto) #mantém habilitada ou não?
    total = 0
    for sent in sents:
        total = total + len(sent)
    return ( total / len (sents) ) 

'''Complexidade de sentença: Média simples do número de frases por sentença.'''

def complexidade_de_sentenca(lista_frases, sentencas):
    lista_sents = separa_sentencas(sentencas) #mantém habilitada ou não?
    lista_frases = separa_frases(sentenca)  #mantém habilitada ou não?
    return (len(lista_frases) / len(lista_sents))
    

'''Tamanho médio de frase: Média simples do número de caracteres por frase.'''

def tamanho_medio_de_frase(lista_frases):
    soma = 0
    for frase in lista frases:
        soma = soma + len(frase)
    return soma


def calcula_assinatura(texto):
     int(input("Entre com um texto:"))
    wal = tamanho_medio_palavras(palavras)
    ttr = relacao_type_token(palavras)
    hlr = razao_hapax_legomana(palavras)
    sal = tamanho_medio_de_sentenca(sents)
    sac = complexidade_de_sentenca(lista_frases, sentencas)
    pal = tamanho_medio_de_frase(lista_frases) 
    
    return [wal, ttr, hlr, sal, sac, pal] #assinatura
    #    ass = []
    #    ass.append


'''Essa funcao recebe duas assinaturas de texto e deve devolver o
grau de similaridade nas assinaturas.'''

def compara_assinatura(as_a, as_b): 
    #comparação de listas
    #if ( ass1 == ass2 ):
    #le_assinatura()
    #as_a = le_assinatura()
    #as_b = calcula_assinatura(texto)
    return ass_cp #lista
    #    abs (differenca( traços)) / 6
    #    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

def avalia_textos(textos, ass_cp):
    #textos = []
    #textos = le_textos()
    #for i in textos:
    #    ass_cp = compara_assinatura(as_a, as_b) #as_a e as_b são as coisas que rodam?
    #    compara_assinatura(orig,i)
    #recebe_comparacao = recebe.comparacao.append(compara_assinatura(i,j))
    return(textos[infectado_POSICAO])
    print("O autor do texto", textos[infectado_POSICAO], "está infectado com COH-PIAH")
    pass
    min = ass_cp[0] 
    k = 1 #como ja tem o temps[0] pode comecar com 1
    while k < len(ass_cp):
        if ass_cp[k] < min:
            min = ass_cp[i]
        k = k + 1
    return min #valor ou posicao do valor?  ira retorna a numeração do texto que esta associada a o valor encontrado.'''

def main():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    le_assinatura()
    continue = True
    t = 1
    textos =  []
    while continue:
        textos.append(textos)
        textos = input("Digite o texto", t, "(aperte enter para sair):")
        t = t + 1
     #cria lista com os textos, como armazenar eles pelo input? Loop?
        
        if input("Digite o texto", t, "(aperte enter para sair):") == "" :
                 continue = False

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


##################################################
#Lista teste
["Conseguiiiiiiiiiiiiiiiiiiiiiiiii", "fazer", "palavras","constitucionalmentesssicissma", "oia", "uia", "só", "sua", "presença", "vai", "me", "deixar", "feliz", "só", "hoje"]






