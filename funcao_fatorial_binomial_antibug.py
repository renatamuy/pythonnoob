def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))
        
def testa_fatorial():
    if fatorial(1) == 1:
        print("Works for 1")
    else:
        print("Does not work for 1")
    if fatorial(2) == 2:
        print("Works for 2")
    else:
        print("Does not work for 2")
    if fatorial(0) == 1:
        print("Works for 0")
    else:
        print("Does not work for 0")
    if fatorial(5) == 120:
        print("Works for 5")
    else:
        print("Does not work for 5")
    




        
        
