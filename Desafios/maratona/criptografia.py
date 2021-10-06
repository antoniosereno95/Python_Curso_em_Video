
nlinhas = input('linhas a serem lidas:')
frase = []
for i in range(len(nlinhas)):
    s = input('digite a frase:')
    frase.append(s)

cripto = []
for i in range(len(nlinhas)):
     f = frase[i].split('')
     print(f)
     #primeiro
     for k in range(len(f)):
        if f[k] in '1234567890':
            pass
        else:
            f[k] = chr(ord(f[k]) + 1)
print(f)





