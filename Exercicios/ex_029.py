vel = input('velocidade: ')
if int(vel) > 80:
    multa = (int(vel)-80)*7
    print('multa de : ', multa,' reais.')
else:
    print('ok, dentro do limite de velocidade')