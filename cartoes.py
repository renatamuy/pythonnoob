meuCartão = int(input("Digite o número do seu cartão"))

cartãolido = 1
encontrei = False
while cartãolido != 0 and not encontrei:
    cartãolido = int(input("Digite o proximo"))
    if cartãolido == meuCartão:
        encontrei = True
if encontrei:
    print("EBA! MEU CARTAO ESTÁ LÁ!!!!")
else:
    print("Xiiiii, meu cartão nao está lá!!!")

#para finalizar o loop, digite um numero de cartao valendo zero
    #é uma forma estranha de finalizar...

    
