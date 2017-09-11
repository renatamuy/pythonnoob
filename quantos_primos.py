
'''Dada uma sequência de números inteiros maiores que um, terminada por um zero, determinar quantos números primos há na sequência.'''

def main():

    num = int(input("Digite um numero (0 para terminar): "))

    cont = 0  # contador de primos
    while num != 0:
        # verifica se num eh primo
        primo = True
        i = 2
        while i < num and primo:
            if num % i == 0:    # se num eh multiplo de i
                primo = False   # num nao pode ser primo
            i += 1
        if primo:
            cont += 1

        num = int(input("Digite um numero (0 para terminar): "))

    print ("Achei %d primos na sequencia"%(cont))

#-----------------------------------------------------
main()
