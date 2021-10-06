soma = 0
for i in range(6):
    n = input('numero:')
    if int(n)%2==0:
        soma = int(soma) + int(i)

print(soma)
