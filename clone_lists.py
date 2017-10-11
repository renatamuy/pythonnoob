'''sublists'''

primos = [2,3,5,7,11,13,17,19,23,29,21,37,39]

primos[1:2] # vai um a menos do que o final! Lembrar diso
# tem só um elemento
primos[2:7]

primos[0:5]
primos[5:len(primos)]

primos[:12] # não precisa inserir o primeiro elemento
primos[12:] # não precisa digitar o último elemento

# Atribuição não é clonagem

lista1 = ["verm", "verde", "azul"]
lista2 = lista1
lista2[0] = "rosa" # altera lista dois e lista 1!!! cuidado..

# Clonar listas no braço

def clone (lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

# fatiamento sempre cria uma nova lista, sem dependencia

lista3 = lista1[0:]
lista4 = lista1[:len(lista1)]
lista5 = lista1[:] # Sweet! Mas é diferente de R....

# Ou seja, funcao clone é desnecessária :P

# Pertencimento a uma lista. Teste lógico:

"rosa" in lista1

if "rosa" in lista2:
    print("Ta sim!")
else:
    print("Xi... ta não!")

# Concatenar listas

[1,2] + [3,4] # Sweet!

print([2,3,4,5] + [2,4,5,6])

a = [1,2,3]
b = [4,5,6]

a + b

b + a

a.append("gato") #isso altera a

a + b # isso não altera a

a + b # pode

b = a + 5 # não pode

b = a + [5] # pode

a_tripled = a * 3 # 3 sequences repeated!

# Removing

del a[1]

del a

lista = ["a", "b", "c", "d", "e", "f"]

del lista[1:5]

####################################################################









