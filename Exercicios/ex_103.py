
def ficha(nome ='',gol = '' ):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0
    print(f'O jogador {nome} marcou {gol} gol(s) no campionato.')


#main
n = input('noma do jogador: ')
g = input('numero de gols: ')
ficha(n,g)