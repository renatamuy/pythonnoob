linha = 1
''' até a tabuada do 10'''
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print (linha * coluna, end = "\t")
        coluna = coluna + 1
        '''quando for pra 11 cai fora do while mais interno'''
    linha = linha + 1
    print ()
    coluna = 1


'''parametro end do print() é = \n, que quer dizer new line,
por isso o default do print é linha, próxima linha.
 Por isso mude para end = " ". Ainda assim, você não resolve o problema,
 pois aí não muda de linha nunca. Então a estratégia é depois do primeiro
print, dar um print vazio só para mudar de linha quando muda o número da tabuada
ou seja, no while mais externo.'''
