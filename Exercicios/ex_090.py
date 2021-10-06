
d = dict()
d['nome'] = str(input('nome: '))
d['nota'] = float(input('nota: '))
if d['nota'] > 7.0:
    d['situ'] ='aprovado'
else:
    d['situ'] ='reprovado'

for k,v in d.items():
    print(f'{k} é igual a {v}')







