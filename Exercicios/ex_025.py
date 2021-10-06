nome = input('nome: ')
nomel = nome.lower()
i = nomel.find('silva')
if i>=0:
    print('tem silva no nome')
else:
    print('nao tem silva no nome')