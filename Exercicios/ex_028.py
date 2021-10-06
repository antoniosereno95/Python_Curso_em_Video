import random
print('começou, chute um nuemro de 0 a 5:')
n = input()
r = random.randint(0,5)
print(r)
if int(r) == int(n):
    print('venceu')
else:
    print('perdeu')








