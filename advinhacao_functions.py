from myfunctions import number_input
from myfunctions import limpar_tela
from random import randint
from time import sleep


def escolha_dificuldade():
    limpar_tela()
    escolha_user = number_input('(1)Fácil  (2)Médio  (3)Difícil  (4)Ultra hard\n Escolha um nível de dificuldade:. ')

    while True:
        # conferindo o que o usuário digitou

        if (escolha_user == 1):  # Fácil
            tentativas = 24
            range = [1, 100]
            pts = 1000
            pts_bonus = 200
            pts_prenda = 300
            print("Nível \033[32mFácil\033[m escolhido")
            break
        elif (escolha_user == 2):  # Médio
            # aqui multiplica o valor do erro por 5
            tentativas = 12
            range = [1, 100]
            pts = 1000
            pts_bonus = 200
            pts_prenda = 300
            print("Nível \033[32mMédio\033[m escolhido")
            break
        elif (escolha_user == 3):  # Difícil
            tentativas = 6
            range = [1, 100]
            pts = 1000
            pts_bonus = 200
            pts_prenda = 300
            print("Nível \033[32mDifícil\033[m escolhido")
            break
        elif (escolha_user == 4):  # Ultra dificil
            tentativas = 3
            range = [1, 100]
            pts = 1000
            pts_bonus = 200
            pts_prenda = 300
            print("Nível \033[32mUltra Hard\033[m escolhido")
            break
        else:
            limpar_tela()
            print(f'\033[31m**ERRO**\033[m ({escolha_user}) é um NÚMERO inválido \033[31m**ERRO**\033[m')
            print("Por Favor escolha uma das opções abaixo\n")
            escolha_user = number_input(
                '(1)Fácil  (2)Médio  (3)Difícil  (4)Ultra hard\n Escolha um nível de dificuldade:. ')
    global dificuldade
    dificuldade = {"tentativa_total": tentativas, "range": range, "pts": pts, "bonus": pts_bonus, "prenda": pts_prenda}
    sleep(2)

# FIM da função escolha_dificuldade()






def menu(x):

    if(x == 1):
        print("\033[31m*\033[m \033[32m*\033[m" * 11)
        print(" Bem-Vindo ao Jogo de Advinhação")
        print("\033[31m*\033[m \033[32m*\033[m" * 11)
        while True:
            escolha_user = number_input('  (1) Iniciar Outra Partida!\n  (2) Iniciar Novo Jogo\n  (3) Ajuda\n  (4) Créditos\n  (5) Sair do JOGO e voltar ao menu principal\n:. ')
            if(escolha_user == 1):# Continuar
                advinhacao(False)
                break
            elif(escolha_user == 2):  # Novo Jogo
                escolha_dificuldade()
                advinhacao(True)
                break
            elif(escolha_user == 3):# ajuda
                print('ajuda')
                break
            elif(escolha_user == 4):#créditos
                print('créditos')
                break
            elif (escolha_user == 5):  # Sair do jogo e voltar ao menu de jogos
                print('tchau')
                break
            else:
                print(f'{escolha_user} não é um número válido')
    elif(x == 0):
        limpar_tela()
        print("\033[31m*\033[m \033[32m*\033[m" * 11)
        print(" Bem-Vindo ao Jogo de Advinhação")
        print("\033[31m*\033[m \033[32m*\033[m" * 11)
        while True:
            escolha_user = number_input('  (1) Novo Jogo\n  (2) Ajuda\n  (3) Créditos\n  (4) Sair do JOGO e voltar ao menu principal\n:. ')
            if(escolha_user == 1):  # Novo Jogo
                return 'novojogo'
                break
            elif(escolha_user == 2):# ajuda
                return 'ajuda'
                break
            elif(escolha_user == 3):#créditos
                return 'creditos'
                break
            elif(escolha_user == 4): #Sair do jogo e voltar ao menu de jogos
                return 'sair'
                break
            else:
                limpar_tela()
                print(f'{escolha_user} não é um número válido')
                print("\033[31m*\033[m \033[32m*\033[m" * 11)
                print(" Bem-Vindo ao Jogo de Advinhação")
                print("\033[31m*\033[m \033[32m*\033[m" * 11)
    else:
        print('caiu no else do menu')
    #Fim da função menu()





def advinhacao(first_time):
    # Número secreto
    inicio = dificuldade['range'][0]
    fim = dificuldade['range'][1]
    numero_secreto = randint(1, (fim))
    limpar_tela()
    print(f'\no número secreto é {numero_secreto}\n')


    # Jogo em si(contando pontos e conferindo se o usuário acertou)
    print("Advinhe o número secreto!")
    sleep(2.5)
    limpar_tela()
    # conferindo se o jogo está iniciando pela primeira vez ou não se sim, ele define os pontos atraves de função dificuldade, se não ele n faz nada e os pontos continuam o msm da antiga partida
    if(first_time == True):
        global pts
        pts = dificuldade['pts']


    for tentativa in range(1, (dificuldade["tentativa_total"] + 1)):
        print(f'tentativa {tentativa} de {dificuldade["tentativa_total"]}')
        print(f'Pontos atuais: {pts}')
        palpite_usuario = number_input(f"Chute um número entre {inicio} e \033[1m{fim}\033[m  ")

        if(palpite_usuario > fim or palpite_usuario < inicio):
            print(f'{palpite_usuario} é um número inválido')
            print('Você perdeu \033[1;31m1\033[m tentativa\n')
            continue

        elif(palpite_usuario == numero_secreto):
            print(f'\033[1;32mParabéns\033[m você acertou na sua {tentativa}° tentativa')
            if(tentativa == 1):
                pts += dificuldade["bonus"]
                print(f'\033[1;32mParabéns\033[m, você ganhou um bônus de \033[1;33m{dificuldade["bonus"]}pts\033[m \npor isso\n')
            pts += tentativa // fim # soma de pontos(qnd o user ganha divide a tentativa atual que ele acertou pelo numero final do rangem e soma aos pontos)
            print(f'Pontos atuais: {pts}')
            sleep(1)
            # Pergunta se quer iniciar novo jogo ou iniciar uma nova partida
            menu(1)
            break
        else:
            if (palpite_usuario > numero_secreto):
                limpar_tela()
                pts -= abs(numero_secreto - palpite_usuario) # perda de pontos(qnd o user perde pega-se a diferença entre onumero secreto e o número que ele chutou e subtrai dos pts)
                print("Você chutou para \033[31mcima\033[m, chute um número \033[32mMenor\033[m\n\n")
            else:
                limpar_tela()
                pts -= abs(numero_secreto - palpite_usuario)  # perda de pontos(qnd o user perde pega-se a diferença entre onumero secreto e o número que ele chutou e subtrai dos pts)
                print("Você chutou para \033[31mbaixo\033[m, chute um número \033[32mMaior\033[m\n\n")
    if(tentativa == dificuldade["tentativa_total"] and palpite_usuario != numero_secreto): # mensagem informando que a pessoa perdeu + pergunta de continuar
        print("Você PERDEU!!!")
        print(f'Como consequência você \033[1;31mperdeu\033[m \033[33m{dificuldade["prenda"]}pts\033[m')
        pts -= dificuldade["prenda"]
        print(f'Pontos atuais: {pts}')
        sleep(1)
        #Pergunta se quer iniciar novo jogo ou iniciar uma nova partida
        menu(1)
# fim da função adivinhação()
