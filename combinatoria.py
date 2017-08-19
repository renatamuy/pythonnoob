#combinatória

#        n!
#________________
#classes!(n - k)!

def fatorial(x):
    fatorialini= 1
    while x > 1:
        fatorialini = fatorialini * x
        x = x - 1
    return fatorialini


#combinacao simples é o coeficiente binomial
#n numero de elementos
    #k de quantos em quantos
    
def combinatoria(n, k):
    sub= n - k
    valor= fatorial(n) / (fatorial(sub) * fatorial(k))

    return(valor)
    




