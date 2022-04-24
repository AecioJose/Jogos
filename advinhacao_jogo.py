from advinhacao_functions import menu, escolha_dificuldade, advinhacao
from myfunctions import limpar_tela


def jogo():
    opção = menu(0)

    if(opção == 'novojogo'):
        escolha_dificuldade()
        advinhacao(True)

    elif(opção == 'ajuda'):
        print('ajuda')

    elif(opção == 'creditos'):
        limpar_tela()
        print('Jogo desenvolvido por Aécio José')
        print('Linkedin: ')
        print('GitHub: ')
        print('Instagram: ')

    elif(opção == 'sair'):
        print('Tchau!!')



'''
ganhar pts acertando --> divide oa tentativa até agr pelo fim e soma no pts
perder diferença entre numero sorteado para chute e subtrai de pts


inplementar:
Sair do menu encerrar jogo
menu de volta ao menu qnd escolher creditos ou ajuda

ir pro menu principal de jogos(outros jogos)
menu com configurações(mini banco de dados)
menu com como usar o programa


subir no git hub >>>>>>>>>>
'''



if(__name__ == "__main__"):
    jogo()