
n = list(input('digite a expressao: '))
print(n)
a = n.count('(')
b = n.count(')')
c = int(a)+int(b)
if int(c)%2==0:
    print('expressao ok')
else:
    print('sua expreçao esta errada')








