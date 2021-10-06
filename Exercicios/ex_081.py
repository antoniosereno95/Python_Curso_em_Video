
lista = []
true = True
while true:
    n = input('digite um numero:')
    lista.append(n)
    resp = str(input('deseja continuar?[s/n]')).lower()
    if resp =='n':
        true = False

print(f'lista original {lista}')
print(f'letra a: {len(lista)}')
lista.sort(reverse=True)
print(f'letra b: {lista}')
c = lista.count('5')
print(f'letra c: o numero 5 aparece {c} vezes.')





