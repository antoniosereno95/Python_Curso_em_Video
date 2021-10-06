d = dict()
gol = list()
jogadores = list()
while True:
    d['nome'] = str(input('nome do jogador: '))
    print(f'quantas partidas {d["nome"]} jogou?',end=' ')
    r = int(input())
    for i in range(r):
        print(f'gols marcados na partida {i+1}:',end=' ')
        g = int(input())
        gol.append(g)
    d['gols'] = gol[:]
    d['total'] = sum(gol)
    #parte nova
    jogadores.append(d.copy())
    d.clear()
    gol.clear()
    resp = str(input('deseja continuar[s/n]')).lower()
    if resp == 'n':
        break
print('_'*20)
print('cod -- nome ----- gols ----- total')
for index_lista,dic_j in enumerate(jogadores):
    print(f'{index_lista} .. {dic_j["nome"]}..... {dic_j["gols"]} ..... {dic_j["total"]}')
print('_'*20)
while True:
    print('_' * 20)
    print('deseja consultar algum jogador em especifico?[s/n]',end='')
    resp = str(input())
    if resp =='n':
        print('Encerrando...')
        break
    print('_' * 20)
    q = int(input('digite o indece do jogador: '))
    while q >= len(jogadores):
        print('indice nao encontrado, tente novamente:')
        q = int(input('indice: '))

    print(f'    Levantamento do jogador: {jogadores[q]["nome"]}')
    for i,v in enumerate(jogadores[q]['gols']):
        print(f'    na partida {i+1} marcou {v} gols')
    print(f'    Total de gols: {jogadores[q]["total"]}')
    print('Fim do levantamendo...')
    print('_' * 20)
