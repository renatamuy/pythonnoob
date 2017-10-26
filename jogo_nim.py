'''Jogo do Nim'''

#pense em N e não em resta?
#n == zero o jogo acabou?

def campeonato():
    partida()
    partida()
    partida()


def partida():
    tipo = int(input("Bem-vindo ao jogo do NIM! Escolha:     1 - para jogar uma partida isolada 2 - para jogar um campeonato 2"))
    if tipo == 1:
        print("Voce escolheu uma partida isolada!")
    usuario_escolhe_jogada()
    '''roda 1 iteracao e diz quem ganhou''' #Como?
    if tipo == 2:
        print("Voce escolheu um campeonato!")
    computador_escolhe_jogada()
    '''roda loop campeonato'''
    if rodada == 1: #Acho que vai ser while ?
                  print('''**** Rodada 1 ****''')
                  quantaspecas = int(input("Quantas peças?"))
                  limitepecas = int(input("Limite de peças por jogada?"))
                  resta = quantaspecas
    if limitepecas//(quantaspecas +1) == 0:
        print("Jogador começa")
        usuario_escolhe_jogada()
    else:
        print("PC começa")
        computador_escolhe_jogada()
while resta > 0:
          usuario_escolhe_jogada()
          if resta == 0 and ganhador == pc:
              print("O computador ganhou!")
          if resta == 0 and ganhador == você:
              print("Você ganhou!")
              placarvoce= placarvoce+1
          else: #sintaxe invalida
              rodada = rodada + 1
              print ("rodada")
if resta == 1:
          print("Fim do jogo! O computador ganhou!")    
          print('**** Final do campeonato! ****')
          print('Placar: Você', placarvoce,'X', placarpc, 'Computador')
          
##############################################
              
def usuario_escolhe_jogada():          
    escolhe = int(input("Quantas peças você vai tirar?"))
    resta = escolhe - quantaspecas
    limitepecas = int(input("Limite de peças por jogada?"))
    print("Agora resta apenas", resta, "peça no tabuleiro.")         
       #resta = quantaspecas - quantaspecas1
#ESSA PARTE É DESNECESSARIA
    if resta > 0 and escolhe > 0 and escolhe <= limitepecas:
        computador_escolhe_jogada()    
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        escolhe = int(input("Quantas peças você vai tirar?")) #Como volto pra cima daqui?
    if resta == 0:
        ganhador == você
        print("Fim do jogo! Você ganhou!")
           
#só dois parametros
#nao vale devolver o número de peças que restam no tabuleiro (acho que estou errando isso)
        
 # funções independentes computador_escolhe_jogada() E usuario_escolhe_jogada()
def computador_escolhe_jogada():
          while pctira < limitepecas:
              pctira = pctira + 1    
              rodadapc= rodadapc+1
          if pctira  //(limitepecas+1) == 0: #Tem que ser verdadeiro
              resta = pctira             
          else:  # se não for possivel
              pctira = limitepecas
              resta = resta - limitepecas
              print("O computador tirou", pctira,"peça.")
              print("Agora restam", resta, "peças no tabuleiro.")
#ESSA PARTE E DESNECESSARIA
          if resta > 0:
              usuario_escolhe_jogada()
          if resta == 0:
              ganhador = pc
              print("Fim do jogo! Você ganhou!")    
            
partida()

'''placar'''
rodada = 1
placarvoce = 0
placarpc =  rodada - placarvoce - 1
pctira = 1
rodadapc = 1


'''fim'''


