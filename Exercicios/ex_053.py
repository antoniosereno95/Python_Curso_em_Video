f = input('frase: ')
f.lower().strip()
f = f.replace(' ','')
palavra = f.split() #transforma em lista
print(palavra)
junto = ''.join(palavra) #pega a lista e tranforma em palavra denovo
print(junto)
inverso = ''

for i in range(len(junto)-1, -1 , -1):
    inverso = inverso + junto[i]


if inverso == junto:
    print('palindromo!')
else:
    print('nops')



