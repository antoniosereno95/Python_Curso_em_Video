
dados = dict()
dados['nome'] = str(input('nome: '))
ano = int(input('ano de nascimento: '))
dados['idade'] = int(2021-ano)
dados['ctps'] = int(input('carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('ano de contrataçao: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = (int(dados['contratacao'])+35)-int(ano)
elif dados['ctps'] == 0:
    dados['ctps'] = str('Nao tem')

for k,v in dados.items():
    print(f'{k} tem valor de {v}')






