
d = dict()
gol = list()

d['nome'] = str(input('nome do jogador: '))
print(f'quantas partidas {d["nome"]} jogou?',end=' ')
r = int(input())
for i in range(r):
    print(f'gols marcados na partida {i+1}:',end=' ')
    g = int(input())
    gol.append(g)
d['gols'] = gol[:]
d['total'] = sum(gol)
print(d)

print(f'O jogador {d["nome"]} jogou {len(d["gols"])} partidas:')
for i,v in enumerate(d['gols']):
    print(f'    =>Na partida {i+1}, fez {v} gols')
print(f'foi um total de {d["total"]} gols maracdos')







