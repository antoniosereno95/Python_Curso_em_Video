n = input('nome da cidade: ')

k = n.lower()
k = k.split(' ')
i = k[0].find('santo')
if i>=0:
    print('tem santo')
else:
    print('nao tem santo')