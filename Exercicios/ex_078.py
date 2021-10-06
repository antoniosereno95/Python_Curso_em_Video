lista = []
for i in range(5):
    n = input('numero: ')
    lista.append(n)
print(lista)

maior = lista[0]
menor = lista[0]
for i in range(len(lista)):
    if int(lista[int(i)]) > int(maior):
        maior = lista[int(i)]
    if int(lista[int(i)]) < int(menor):
        menor = lista[int(i)]

print(f'maior: {maior}, menor:{menor}')







