import random
r = random.randint(0,10)
count = 1
n = input('numero de 0 a 10: ')

while int(n) != int(r):
    print('tente novamente: ')
    count += 1
    n = input()

print('parabens voce acretou em ',count,' chances.')
