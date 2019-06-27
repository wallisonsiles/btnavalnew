from btnaval import Partida
from datetime import datetime
import random
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"
REVERSE = "\033[;7m"
random.seed(datetime.now())
alfabeto = ( ('A','B', 'C', 'D','E','F','G','H','I','J','K', 'L','M','N','O','P','Q', 'R','S','T','U','V','W', 'X', 'Y', ' '))
def print_board(board):

    for row in board:

        for i in range(1):

                for j in range(14):
                        while i <  15:

                            print( " ",i," " ,end =  '')

                            i += 1
                        print("\n"+ alfabeto[j] + "" + " ".join(row),end = " ")
def imprime(tab, pontos, tiros, ptab):

        print('\nPontuação: ', pontos, end="     ")
        print('     Tiros: ', tiros, end="\n")
        for j in range(0, 15):
            print(alfabeto[j-1], end="")
            if j == 0:
                b = 0
                while (b < 15):
                    if b==0:
                        print(end="  | ")
                        b += 1
                    else:
                        if b<9:
                            print(b , end=" | ")

                        else:
                            if b==14:
                                print(b, end=" |")
                            else:
                                print(b , end=" |")
                        b += 1
            else:
                for i in range(0, 15):


                            if tab[i][j][2]:
                                if tab[i][j][0] == 'A':
                                        print(CYAN+'O'+RESET, end=" | ")
                                else:
                                        print(RED+'X'+ RESET, end=" | ")
                            else:
                                print(' ', end=" | ")
            print()
        print('Submarinos:\t', ptab.submarinos)
        print('Destroyers:\t', ptab.destroyers)
        print('Hidro-aviões:\t', ptab.hidros)
        print('Cruzadores:\t', ptab.cruzadores)
        print('Couraçados:\t', ptab.couracados)

def imprimePF(pontos, tiros, tempo, ptab):
        print('\nPontuação final: ', pontos)
        print('Tiros restantes: ', tiros)
        print('Tempo: ', tempo)
        print('Submarinos restantes:\t', ptab.submarinos)
        print('Destroyers restantes:\t', ptab.destroyers)
        print('Hidro-aviões restantes:\t', ptab.hidros)
        print('Cruzadores restantes:\t', ptab.cruzadores)
        print('Couraçados restantes:\t', ptab.couracados)


        

p = Partida()
imprime(p.tabuleiro.matriz, p.pontos, p.tiros, p.tabuleiro)
while True:
        while True:
            pos = (random.randint(1,15), random.randint(1,15))
            if p.jogar(pos[0], pos[1]):
                break
        imprime(p.tabuleiro.matriz, p.pontos, p.tiros, p.tabuleiro) #comente essa linha para ter resultados rápidos
        if p.finaliza():
                break
imprimePF(p.pontos, p.tiros, p.tempo, p.tabuleiro)
