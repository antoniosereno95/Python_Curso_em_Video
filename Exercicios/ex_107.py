import moeda

inteiro = int(input('digite um int: '))
floate = float(input('digite um float: '))

ia = moeda.aumentar(inteiro)
id = moeda.diminuir(inteiro)
ido = moeda.dobro(inteiro)
ime = moeda.metade(inteiro)
print(f' {inteiro}; aumenta = {ia} ;diminuir = {id} ; dobro = {ido} ; metade {ime}')
fa = moeda.aumentar(floate)
fd = moeda.diminuir(floate)
fdo = moeda.dobro(floate)
fme = moeda.metade(floate)
print(f' {floate}; aumenta = {fa} ;diminuir = {fd} ; dobro = {fdo} ; metade {fme}')




