
def primo(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return not n % 2 == 0 
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k = k + 2
    else:
        return True



def maior_primo(i):             
    if (primo(i)):
        return(i)
    else:
        roda = i
    while roda >= 2:
        if primo(roda) == True:
            return(roda)
        else:
            roda = roda - 1
    print(roda)
        
