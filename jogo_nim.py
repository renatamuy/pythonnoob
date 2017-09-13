'''Jogo do Nim'''
def partida():
    tipo = input("Bem-vindo ao jogo do NIM! Escolha:
    1 - para jogar uma partida isolada
    2 - para jogar um campeonato 2")
    if tipo == 1:
    print("Voce escolheu uma partida isolada!)
    '''roda 1 iteracao e diz quem ganhou''' #Como?
else:
    print("Voce escolheu um campeonato!")
    '''roda loop campeonato'''

'''placar'''

placarvoce = quantasganhou
placarpc =  totalrodadas- placarvoce
 
if resta = 1:
          print("Fim do jogo! O computador ganhou!")    
          print('**** Final do campeonato! ****')
          print('Placar: Você', placarvoce,'X', placarpc, 'Computador')
rodada =1      
while resta>0:
          usuario_escolhe_jogada()
          if resta == 0 and ganhador = pc:
          print("O computador ganhou!")
          if resta == 0 and ganhador = você:
          print("Você ganhou!")
    else:
          rodada= rodada + 1
          print rodada

if rodada = 1: #Acho que vai ser while né? e rodada será i?
          print('''**** Rodada 1 ****''')
        quantaspecas = input("Quantas peças?")
        limitepecas = input("Limite de peças por jogada?")

if limitepecas//(quantaspecas +1) == 0:
          print("Jogador começa")
        else:
          print("PC começa")
          
def usuario_escolhe_jogada():          
    escolhe = int(input("Quantas peças você vai tirar?"))
    resta = quantaspecas - escolhe
    print("Agora resta apenas", resta, "peça no tabuleiro.")         
    else:
    resta = quantaspecas - quantaspecas1
        if resta > 0 and escolhe > 0 and escolhe <= limitepecas:
       computador_escolhe_jogada()    
        else:
        print("Oops! Jogada inválida! Tente de novo.")
        escolhe = int(input("Quantas peças você vai tirar?")) #Como volto pra cima daqui?
        if resta = 0:
        ganhador = você
        print("Fim do jogo! Você ganhou!")    
          
def computador_escolhe_jogada(limitepecas, quantaspecas):
          pctira = ????? #estratégia 
          if resta  //(limitepecas+1) == 0 #Tem que ser verdadeiro

          else  # se não for possivel
          pctira = limitepecas
          resta = resta - limitepecas
          print("O computador tirou", pctira,"peça.")
          print("Agora restam", resta, "peças no tabuleiro.")
          if resta > 0:
          usuario_escolhe_jogada()
          if resta = 0:
          ganhador = pc
          print("Fim do jogo! Você ganhou!")    
              
'''fim'''
