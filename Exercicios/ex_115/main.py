from lib import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo nao encontrado.')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa','Sair do sistema'])
    if int(resposta) == 1:
        #ler o arquivo
        lerArquivo(nome=arq)
    elif int(resposta) == 2:
        #add no arquivo
        cabeçalho('Novo Cadastro')
        nome = str(input('nome: '))
        idade = int(input('idade: '))
        cadastrar(arq,nome,idade)

    elif int(resposta) == 3:
        print(cabeçalho('Saindo do Sistema...'))
        break




