#modulos lib

def linha( tam = 42):
    return '_'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'    {c} - {item}')
        c += 1
    print(linha())
    resp = input('digite o numero da sua opçao: ')
    while str(resp) not in '123':
        print(linha())
        resp = input('entrada errada, tente novamente\ndigite o numero da sua opçao: ')
    return resp



