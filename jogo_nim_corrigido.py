'''Jogo do Nim'''

tipo_jogo = 0

def usuario_escolhe_jogada(n,m):          
    jogada = 0
    while jogada == 0:

        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
    return jogada


def computador_escolhe_jogada(n, m):
    if n<= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
         
        return m
    
        print("O computador tirou",m,"peça.")
        print("Agora restam", quantia, "peças no tabuleiro.")


def partida():
     
    #print(" ")

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    is_computer_turn = True
     
    if n % (m+1) == 0: is_computer_turn = False

    while n > 0:
         
        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("O computador tirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você tirou {} peças.".format(jogada))

        n = n - jogada

        print("Agora resta apenas {} peças no tabuleiro.\n".format(n))
         
    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def campeonato():
     
    # Pontuações:
    usuario = 0
    computador = 0
     
    # Executa 3 vezes:
    for _ in range(3):
         
        # Executa a partida:
        vencedor = partida()
         
        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1
             
    # Exibe o placar final:
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))
     


while tipo_jogo == 0:
     
    # Menu de opções:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
   
     
    # Solicita a opção ao usuário:
    tipo_jogo = int(input("2 - Para jogar um campeonato "))
    print(" ")
 
    # Decide o tipo de jogo:
    if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
    if tipo_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        tipo_jogo = 0



##############################################


'''fim'''


