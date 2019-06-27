from btnaval import Partida

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"
REVERSE = "\033[;7m"

alfabeto = ( ('A','B', 'C', 'D','E','F','G','H','I','J','K', 'L','M','N','O','P','Q', 'R','S','T','U','V','W', 'X', 'Y', ' '))
pontos = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11, 'L':12,'M':13,'N':14}

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
            print("| ", end="")
            for i in range(0, 14):
                    if tab[i][j][2]:
                        if tab[i][j][0] == 'A':
                                print('O', end=" | ")
                        else:
                                print('X', end=" | ")
                    else:
                        print(' ', end=" | ")
            print()
        print('Submarinos:\t', ptab.submarinos)
        print('Destroyers:\t', ptab.destroyers)
        print('Hidro-aviões:\t', ptab.hidros)
        print('Cruzadores:\t', ptab.cruzadores)
        print('Couraçados:\t', ptab.couracados)
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
                                        print('O', end=" | ")
                                else:
                                        print('X', end=" | ")
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
                x, y = input('\n coordenadas: ').split()
                try:

                        if p.jogar(int(x), int(pontos[y])):

                                break
                except:
                        pass
        imprime(p.tabuleiro.matriz, p.pontos, p.tiros, p.tabuleiro)
        if p.finaliza():
                break
imprimePF(p.pontos, p.tiros, p.tempo, p.tabuleiro)
