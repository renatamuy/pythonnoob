'''remove_repetidos recebe uma lista com inteiros, verifica os elementos repetidos
e os remove em uma lista correspondente a primeira lista sem repetidos e ordenada'''

#lista = [200000,1,2,3,3,3,3,5,3,9,9,8,8, 100000,  20]

def remove_repetidos(lista):
    #lista = input("Insira sua lista aqui")
    i = 0
    listanova = lista[:]
    listanovinha = lista[:]
    for i in range(0, len(lista)):
        valor = lista[i]
        listanova.remove(valor)
        if valor in listanova:
            listanovinha.remove(valor)
    lista = sorted(listanovinha[:])
    #lista= listanovinha.sort()
    return(lista)
    #print(type(lista))


#Eu só tinha esquecido de dar return??
#remove_repetidos(lista)    


####################################################################################
#Outra maneira!
#Eu queria mudar a lista no loop. Isso não funciona pois o comprimento dela vai mudando
#listavazia = []
#i = 0

#def remove_repetidos(lista):
#    for i in lista:
#        if i not in listavazia: 
#            listavazia.append(i)
#    #listinha= list(listavazia[:])        
#    return(listavazia)
#    print(type(listavazia))
#    return(sorted(listavazia))

#remove_repetidos(lista)




