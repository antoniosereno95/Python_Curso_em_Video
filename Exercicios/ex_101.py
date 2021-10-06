
def voto(ano):
    idade = int(2021 - int(ano))
    re = ''
    if idade < 18:
        re = f'indiciduos com {idade} nao votam.'
    elif idade >= 18 and idade < 65:
        re = f'cidadoes com {idade} tem voto obrigatorio.'
    elif idade >= 65:
        re = f'cidadoes com {idade} tem voto opcional'
    return re


#main
i = input('data de nascimento: ')
r = voto(i)
print(r)





