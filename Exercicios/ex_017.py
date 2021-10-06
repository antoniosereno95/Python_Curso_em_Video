import math
co = input('catto oposto: ')
ca = input('cateto adjacente: ')

hip = math.sqrt(math.pow(float(co),2) + math.pow(float(ca),2))
print(hip)
#ou
hipp = math.hypot(float(ca),float(co))
print(hipp)