def fatorial(k):
    '''(int) -> int

    Receive a integer number and returns k!

    Assumes k is an integer and positive number
    '''

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # same as cont = cont + 1
        k_fat *= cont   # same as k_fat = k_fat * cont

    return k_fat
