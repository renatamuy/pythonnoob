'''Tamanho médio de palavra: Média simples do número de caracteres por palavra.
Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
Tamanho médio de sentença: Média simples do número de caracteres por sentença.
Complexidade de sentença: Média simples do número de frases por sentença.
Tamanho médio de frase: Média simples do número de caracteres por frase.
Lista de funções
OK def le_assinatura():
OK def le_textos():
OK def separa_sentencas(texto):
OK def separa_frases(sentenca):
OK def separa_palavras(frase):
OK def n_palavras_unicas(lista_palavras):
OK def n_palavras_diferentes(lista_palavras):
OK def compara_assinatura(as_a, as_b): 
OK20 def calcula_assinatura(texto): 
def avalia_textos(textos, ass_cp): 
OK19 def tamanho_medio_palavras(palavras):
OK19 def relacao_type_token(palavras):
OK19 def razao_hapax_legomana(palavras):
OK19 def tamanho_medio_de_sentenca(sentencas):
OK19 def complexidade_de_sentenca(lista_frases, sentencas):
OK19 def tamanho_medio_de_frase(lista_frases):
OK19 def main()
'''

####################################################################
import re
           
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''


def le_assinatura():
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

'''Tamanho médio de sentença: Média simples do número de caracteres por sentença.'''

def tamanho_medio_de_sentenca(sentencas):
    total = 0
    for sent in sentencas:
        total = total + len(sent)
    return ( total / len (sentencas) ) 

'''Complexidade de sentença: Média simples do número de frases por sentença.'''

def complexidade_de_sentenca(lista_frases, sentencas):
    return len(lista_frases) / len(sentencas)
    
'''Tamanho médio de frase: Média simples do número de caracteres por frase.'''

def tamanho_medio_de_frase(lista_frases):
    soma = 0
    for frase in lista_frases:
        soma = soma + len(frase)
    return soma / len(lista_frases)

def calcula_assinatura(texto):
    #Crie uma lista de sentencas
    sentencas = separa_sentencas(texto)
    #Crie uma lista de frases
    frases = []
    for s in sentencas:
        frases_separadas = separa_frases(s)
        for fs in frases_separadas:
            frases.append(fs)           

    #Crie uma lista de palavras (palavras)
    palavras = []
    for ps in frases:
        palavras_seps = separa_palavras(ps)
        for palsep in palavras_seps:
            palavras.append(palsep)
    
    #Crie uma lista para receber as assinaturas
    
    a = tamanho_medio_palavras(palavras)
    b = relacao_type_token(palavras)
    c = razao_hapax_legomana(palavras)
    d = tamanho_medio_de_sentenca(sentencas)
    e = complexidade_de_sentenca(frases, sentencas)
    f = tamanho_medio_de_frase(frases)
    
    assinatura = [a, b, c, d, e, f]
    
    return assinatura


'''Essa funcao recebe duas assinaturas de texto e deve devolver o
grau de similaridade nas assinaturas.'''

#as_a já sai como float?

def compara_assinatura(as_a, as_b):
    somadiferenca = 0 
    for i in range(len(as_b)):
        somadiferenca = somadiferenca + abs(as_a[i] - as_b[i])
    similaridade_a_b = somadiferenca / 6
    return similaridade_a_b


#list indices must be integers or slices, not float

'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero
(1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

def avalia_textos(textos, assinaturas_comp):
    min = assinaturas_comp[0] 
    for k in range(len(assinaturas_comp)):
        if ass_cp[k] < min:
            min = assinaturas_comp[k]
    return k #deve se retornar k e não min grrrrr eu temia cometer esse erro desde o princípio


'''Essa função amarra tudo'''

def main():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    assinatura_input = le_assinatura()
    textos = le_textos() #pode ser uma lista normal
    assinaturas = []
    
    for texto in textos:
        assinaturas.append( calcula_assinatura(texto))

    assinaturas_comp = []
    
    for assinatura in assinaturas:
        assinaturas_comp.append( compara_assinatura(assinatura_input, assinatura))

    infectado = avalia_textos(textos, assinaturas_comp)
    print(" ")
    print("O autor do texto ", infectado, " está infectado com COH-PIAH")


#Chama a função pra começar o programa
main()


