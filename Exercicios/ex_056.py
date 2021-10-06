soma_id = 0
id_velho = 0
nome_velho = ''
cont_mulher = 0

for i in range(4):
    print('idade ',i)
    id = input()
    print('nome: ',i)
    nome = input()
    print('sexo(m/f) ',i)
    sexo = input()
    soma_id += int(id)
    if str(sexo)=='f' and int(id)<20:
        cont_mulher+=1
    if int(id) > int(id_velho) and sexo=='m':
        id_velho = id
        nome_velho = nome

media = soma_id/4
print('media id: ',media)
print('nome velho: ',nome_velho)
print('mulher menor q 20: ',cont_mulher)

